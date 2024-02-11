from openai import OpenAI
import streamlit as st
from core.innSight import InnSight
from streamlit_option_menu import option_menu 

import About



with st.sidebar: 
    selected = option_menu(
        menu_title=None,
        options=["Chat", "About the Project"],
    )

inn_sight = InnSight()

if selected == "About the Project":
    About.show()
else:
    st.title("InnSight")
    st.write('Our project for the generative AI track')
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What are your travel concerns?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):        
            prompt = st.session_state.messages[-1]['content']
            result = inn_sight.answer_user_prompt(prompt)
            st.write(result)
        st.session_state.messages.append({"role": "assistant", "content": result})