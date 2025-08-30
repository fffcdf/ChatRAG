import streamlit as st
import requests

st.set_page_config('ChatRAG')

st.title('ChatRAG')
st.markdown('You can ask him anything about Unilever, what can be possibly on unilever-annual-report-and-accounts (2022,2023,2024)')

call_text=st.text_area('Question for ChatRAG',height=300,placeholder='Enter the question for ChatRAG')

if st.button('Ask RAG'):
        if call_text.strip() == "":
            st.warning('Please enter the question for ChatRAG')
        else:
            try:
                response=requests.post(
                    'http://127.0.0.1:8000/ask/',
                    json={"query":call_text}
                )
                if response.status_code==200:
                    result=response.json()
                    st.subheader('Reply from RAG')
                    st.text(result)
                else:
                    st.error(f"Error server: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Error API: {e}")
