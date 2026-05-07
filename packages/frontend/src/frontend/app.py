import streamlit as st 
from backend.constants import ROOT_PATH
import httpx
import os 

API_URL = os.getenv("API_URL","http://localhost:8000")

def layout():
    st.set_page_config(page_title="WIRED-AL", page_icon=f"{ROOT_PATH}/assets/favicon-96x96.png")
    
    with st.sidebar:
        st.image(f"{ROOT_PATH}/assets/logo-dark.png")
        st.markdown("AI onboarding copilot")

        st.divider()
        st.markdown("### Knowledge Base")
        
        st.info("Company documents will be available here.")
    
    
    
    st.markdown("# WIRED-AL")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! I am your onboarding copilot. Ask me anything about onboarding."
            }
        ]
    
    st.divider()
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    user_question = st.chat_input("Ask a question")        
    
    if user_question:
        st.session_state.messages.append(
            {"role": "user", "content": user_question}
            )
        
        with st.chat_message("user"):
            st.markdown(user_question)
            
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = httpx.post(
                    f"{API_URL}/ask", 
                    json={"question": user_question}, 
                    timeout=120
        )
                    response.raise_for_status()
                    data = response.json()
                
                    answer = data.get("answer", "I could not find an answer.")
                    sources = data.get("sources")
                
                    st.markdown(answer)
                
                    if sources:
                     with st.expander("Sources"):
                         for source in sources:
                             document_name = source.get("document_name", "Unknown document")
                             content_preview = source.get("content_preview", "")
                             
                             clean_preview = (
                                content_preview
                                .replace("#", "")
                                .replace("\n", " ")
                                .replace(document_name, "")
                                .strip()
                            )
                             
                             st.markdown(f"**{document_name}**")
                             
                             if clean_preview:
                                 st.markdown(clean_preview[:180] + "...")
                                 
                                 st.divider()
                        
                    assistant_message = answer
                
                    if sources:
                        source_name = [
                            source.get("document_name","Unknown document")
                            for source in sources
                        ]
                        
                        assistant_message += "\n\n**Sources:**\n"
                        assistant_message +="\n".join(
                            [f"-{name}" for name in source_name]
                        )
                        
                    
                    st.session_state.messages.append(
                        {"role": "assistant", "content": assistant_message}
                )
                
                except httpx.RequestError:
                    error_message = "Colud not connect to the backend API."
                    st.error(error_message)
                    
                except httpx.HTTPStatusError:
                    error_message = "The backend returned an error"
                    st.error(error_message)
                    
        


if __name__ == "__main__":
    layout()
        
    