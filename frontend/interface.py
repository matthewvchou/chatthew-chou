import streamlit as st
import time

st.set_page_config(layout="wide")

# Initialize navigation state
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False

# Intro Page
if not st.session_state.show_chat:
    st.title("👋 Welcome to Chat-thew Chou!")
    st.markdown("""
        I'm Chat-thew — a fun little personal chatbot you can talk to.

        - Click below to start chatting
        - Or browse around using the sidebar
    """)
    if st.button("👉 Enter Chat", use_container_width=True):
        st.session_state.show_chat = True
        st.rerun()

# Chat Page
else:
    st.title("Chat-thew Chou")

    # Initialize messages
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "chatthew", "content": "Hey there! I'm Chat-thew Chou 😎\n\nAsk me anything or type `--help` for more!"}
        ]

    # Sidebar
    with st.sidebar:
        st.markdown("**Projects & Experience**")
        top = st.container()
        with top:
            st.link_button(label="LinkedIn", url="https://www.linkedin.com/in/chou-matthew/", icon=":material/cheer:", use_container_width=True)
            st.link_button(label="GitHub", url="https://github.com/matthewvchou", icon=":material/hub:", use_container_width=True)
            st.button("Resume", icon=":material/download:", use_container_width=True)  # Not yet implemented
        
        st.markdown("**Fun Stuff :D**")
        fun = st.container()
        with fun:
            st.button(label="About Me", icon=":material/boy:", use_container_width=True)

        # Bug report button container
        st.markdown("**Contact Me**")
        contact = st.container()
        with contact:
            st.button("Email Me", icon=":material/mail:", use_container_width=True)
            st.button("Report a Bug", key="bug_button", icon=":material/bug_report:", use_container_width=True)

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User Input
    if prompt := st.chat_input("Type \"--help\" for more info"):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Chat-thew Response
        response = f"{prompt}"

        def stream_response():
            for char in response:
                yield char
                time.sleep(0.025)

        with st.chat_message("chatthew"):
            st.write_stream(stream_response)
        st.session_state.messages.append({"role": "chatthew", "content": response})
