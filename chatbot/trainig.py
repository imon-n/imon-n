import streamlit as st

st.title("Training Interface for Stellar's Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [
        {'user': 'Customer', 'message': 'Are you human?', 'time': '07-05-2024 10:00'},
        {'user': 'Chatbot', 'message': 'No, I am not human, but I can help you anytime.', 'time': '07-05-2024 10:00'},
        {'user': 'Customer', 'message': 'Are all products available?', 'time': '06-05-2024 17:02'},
        {'user': 'Chatbot', 'message': 'Yes, all products are available.', 'time': '06-05-2024 17:03'}
    ]

st.header("Recent Chatting Interactions")

for chat in st.session_state['chat_history']:
    st.write(f"{chat['time']} - {chat['user']}: {chat['message']}")


st.header("Edit Response")

customer_questions = []

for chat in st.session_state['chat_history']:
    if chat['user'] == "Customer":
        customer_questions.append(chat['message'])


question_edit = st.selectbox("Choose a question to edit:", options=customer_questions)
correct_response = st.text_input("Correct response:")

if st.button("Save Edited Response"):
    if question_edit and correct_response:
        st.write(f"Saved corrected response for '{question_edit}': '{correct_response}'")


st.header("Add New Training Data")

new_question = st.text_input("New question:")
new_answer = st.text_input("New answer:")

if st.button("Add to Training"):
    st.write(f"Added new training data: '{new_question}' -> '{new_answer}'")
