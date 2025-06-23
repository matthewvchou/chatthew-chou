import streamlit as st

# Creating instance
st.title("Chat-thew Chou")
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    linkedin = st.link_button(label="LinkedIn", url="https://www.linkedin.com/in/chou-matthew/", icon=":material/cheer:", use_container_width=True)
    github = st.link_button(label="GitHub", url="https://github.com/matthewvchou", icon=":material/hub:", use_container_width=True)
    email = st.button("Email Me", icon=":material/mail:", use_container_width=True)
    resume = st.button("Resume", icon=":material/download:", use_container_width=True) # Need to implement

# ???
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("What's up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user",
                                      "content": prompt})
    
# Chat-thew Response
response = f"Echo: {prompt}"
with st.chat_message("chatthew"):
    st.markdown(response)
st.session_state.messages.append({"role": "chatthew",
                                  "content": response})