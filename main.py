from langchain_ollama import ChatOllama,OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.pydantic_v1 import BaseModel

model_name='llama3.1:8b'
llm=ChatOllama(model=model_name)
embeddings=OllamaEmbeddings(model='nomic-embed-text:v1.5')

# в случае создания бд
#from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
#from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader=DirectoryLoader("docs for db/",glob="**/*.pdf",loader_cls=PyPDFLoader)
# docs=loader.load()
# text_splitter=RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=500)
# all_splits=text_splitter.split_documents(docs)

#vectorstore=Chroma(documents=all_splits,embedding=embeddings,persist_directory='./chroma_db')

vectorstore=Chroma(embedding_function=embeddings,persist_directory='./chroma_db')
retriever = vectorstore.as_retriever()

template="""Your job is to answers questions about Unilever.
Use the following context to answer questions. Be as detailed
as possible, but don't make up any information that's not
from the context. If you don't know an answer, say you don't know.
Don't invent anything.

Context:
{context}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | llm
    | StrOutputParser()
)

class Question(BaseModel):
    __root__: str

chain = chain.with_types(input_type=Question)
