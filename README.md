# ChatRAG
RAG с UI через Streamlit, а также Ollama для локального LLM.  
Сделан через LangChain и язык LCEL для chain, а также FastAPI для API.  
Для векторной базы данных была выбрана Chroma.  

Этот RAG создан для того чтобы быстро находить информацию среди отчетов компании.  
Были использованы ежегодные отчёты компании Unilever в качестве примера документов, которые можно найти в открытом доступе.   
Язык: Английский.    

В качестве LLM выбрана [llama3.1:8b](https://ollama.com/library/llama3.1). 
Для её запуска необходимо ввести в консоль ollama pull llama3.1:8b.  

Для запуска Streamlit необходимо ввести в терминал ```streamlit run st.py```.      
Для запуска API необходимо ввести в терминал```uvicorn app:api --reload``` .   



<img width="778" height="575" alt="image" src="https://github.com/user-attachments/assets/0ad4cbd2-4e88-41dc-8c11-0efd738b8107" />
