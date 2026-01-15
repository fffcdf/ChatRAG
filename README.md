# ChatRAG
Структура проекта:  
● UI - Streamlit.  
● LLM - Ollama [llama3.1:8b](https://ollama.com/library/llama3.1).  
● Agents - LangChain.  
● API - FastAPI.  
● VectorDB - Chroma.  
● Langauge - English.  

Реализованы следующие функции:  
● Быстрый поиск информации среди отчетов компании.  
● Выполнение различных подсчётов, связанных с документами.  

Были использованы документы компании Unilever, которые можно найти в открытом доступе.   

Команда запуска LLM - ```ollama pull llama3.1:8b```.  
Команда запуска API - ```uvicorn app:api --reload``` .   
Команда запуска Streamlit - ```streamlit run st.py```.     

Демонстрационное фото интерфейса:  
<img width="778" height="575" alt="image" src="https://github.com/user-attachments/assets/0ad4cbd2-4e88-41dc-8c11-0efd738b8107" />
