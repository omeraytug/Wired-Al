import streamlit as st 
import httpx
import os 

API_URL = os.getenv("API_URL","http://localhost:8000")

def layout():
    st.markdown("# 404 brain not found ")
    st.markdown("Ask me about onboarding")
    
    text_input = st.text_input(label="Ask a question")
    
    if st.button("send") and text_input.strip() != "":
        response = httpx.post(
            f"{API_URL}/ask", json={"question": text_input}, timeout=120
        )
        
        data = response.json()
        
        st.markdown("## Question")
        st.markdown(text_input)
        
        st.markdown("## Answer")
        st.markdown(data.get("answer"))
        
        st.markdown("## Source")
        st.markdown(data.get("sources"))


if __name__ == "__main__":
    layout()
        
    