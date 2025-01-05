import os
import csv
import datetime
from typing import Literal, TypeAlias
from dataclasses import dataclass
from sklearn.metrics import accuracy_score, classification_report
import streamlit.components.v1 as components
import streamlit as st
from chatbot import chat_bot, X_test,y_test,clf

@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str

def load_css():
    try:
         with open("static/style.css", "r") as f:
            css = f"<style>{f.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError: st.error("CSS file not found.") 
    except Exception as e: st.error(f"An error occurred: {e}")

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    response = chat_bot(human_prompt)
    st.session_state.history.append(Message("human", human_prompt))
    st.session_state.history.append(Message("ai", response))

load_css()



    # creating side bar
menue=["🏠Home","ℹ️ About","📄Source Code"]
choice =st.sidebar.selectbox("Menue",menue)







 
if choice == "🏠Home":
   
    
    initialize_session_state()
     
    st.write(
         """
          <div class="title"> SUPRV GPT </div>
        """,
    unsafe_allow_html=True
)

    chat_placeholder = st.container()
    prompt_placeholder = st.form("Chat-form")

 
    

    with chat_placeholder:
        for chat in st.session_state.history:
            div = f"""
    <div class="chat-row
        {'' if chat.origin =='ai' else 'row-reverse'}">
        <img class="chat-icon" src="app/static/{
            'bot.jpeg' if chat.origin == 'ai'
                        else 'user.png'}
            "width=32 height=32>
        <div class="chat-bubble
        {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
            &#8203;{chat.message}
        </div>
    </div>
        """
            st.markdown(div, unsafe_allow_html=True)
            
            
        for _ in range(3):
            st.markdown("")

    with prompt_placeholder:
        st.markdown("Chat with Me")
        cols = st.columns((6, 1))
        cols[0].text_input("chat", value="Hello", label_visibility="collapsed", key="human_prompt",)
        cols[1].form_submit_button("Submit", type="primary", on_click=on_click_callback,)





        components.html("""
    <script>
    const streamlitDoc = window.parent.document;

    const buttons = Array.from(
        streamlitDoc.querySelectorAll('.stButton > button')
    );
    const submitButton = buttons.find(
        el => el.innerText === 'Submit'
    );

    streamlitDoc.addEventListener('keydown', function(e) {
        switch (e.key) {
            case 'Enter':
                submitButton.click();
                break;
        }
    });
    </script>
    """, 
        height=0,
        width=0,
    )
        
elif choice== "ℹ️ About":
         st.title("About Me: SUPRV GPT")
         st.write("SUPRV GPT is an AI-powered chatbot designed to streamline and enhance customer interactions in the accommodation rental domain. Utilizing cutting-edge Natural Language Processing (NLP) techniques, this chatbot delivers fast, accurate, and contextually relevant responses to user queries. Built with Python, NLTK, and TensorFlow, SUPRV GPT is tailored for scalability, user engagement, and operational efficiency.")

         st.write("""This chatbot project is a conversational AI system designed to understand and respond to user queries. 
                Built using Python, Natural Language Processing (NLP) techniques, and the Logistic Regression algorithm, 
                the chatbot provides a user-friendly interface through the Streamlit web framework.""")

         st.header("Key Achievements")
         st.write(
             """
                <div class="list">
                    <ul>
                        <li> This chatbot effectively utilizes NLP techniques to understand user input. </li>
                        <li> The Logistic Regression algorithm is successfully employed to classify user input. </li>
                        <li> The Streamlit web framework provides an intuitive and interactive interface. </li>
                        <li> This chatbot understands user input properly. </li>
                        <li> Generates suitable responses to user queries. </li>
                    </ul>
                </div>
                  
             """,
                 unsafe_allow_html=True
             )
         st.header("Developer")
         st.write(
             """
                <h4> <center> Rahul Ji Ara </center> </h4>
                <div class= "socialmedia">
                    <a href="https://www.github.com/rahuljiara" target ="_blank" class="social-media-btn"> 
                    <img src="https://cdn-icons-png.flaticon.com/128/2111/2111425.png" class="social-media-btn_img"> 
                Github </a>
                  
                <a href="https://www.facebook.com/rahuljiara" target ="_blank" class="social-media-btn"> 
                    <img src="https://cdn-icons-png.flaticon.com/128/733/733547.png" class="social-media-btn_img"> 
                Facebook </a>
                  
                <a href="https://www.instagram.com/rahuljiara" target ="_blank" class="social-media-btn"> 
                    <img src="https://cdn-icons-png.flaticon.com/128/2111/2111463.png" class="social-media-btn_img"> 
                Instagram </a>
                </div>
                
                  
                  
             """,
                 unsafe_allow_html=True
             )
    
         
elif choice== "📄Source Code":
         st.title("Rahul Ji Ara")
         st.markdown(
    """
    <a href="https://github.com/rahuljiara/suprv-gpt" target="_blank">
        <button class="source_code_btn">
            Download Source Code
        </button>
    </a>
    """,
    unsafe_allow_html=True
)


