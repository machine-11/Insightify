import streamlit as st
# import json
from logics import gen_quiz
import Insightify

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Title and description

st.title("Quiz")
st.subheader("All about buying new flats")

# st.sidebar.markdown(Insightify.md)

# Custom CSS for the buttons
st.markdown("""
<style>
div.stButton > button:first-child {
    display: block;
    margin: 0 auto;
</style>
""", unsafe_allow_html=True)

st.markdown("""
            <style>.big-font {font-size: 120px ;}</style>
            """, unsafe_allow_html=True)


# Initialize session variables if they do not exist
default_values = {'quiz_data': None , 'current_index': 0, 'current_question': 0, 'score': 0, 'selected_option': None, 'answer_submitted': False}
for key, value in default_values.items():
    st.session_state.setdefault(key, value)


def start_quiz():
    st.session_state.quiz_data = gen_quiz.gen_quiz()
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False


# def restart_quiz():
#     start_quiz()


def submit_answer():

    # Check if an option has been selected
    if st.session_state.selected_option is not None:
        # Mark the answer as submitted
        st.session_state.answer_submitted = True
        # Check if the selected option is correct
        if st.session_state.selected_option ==  st.session_state.quiz_data[st.session_state.current_index]['answer']:
            st.session_state.score += 10
    else:
        # If no option selected, show a message and do not mark as submitted
        st.warning("Please select an option before submitting.")

def next_question():
    st.session_state.current_index += 1
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False



if st.session_state.quiz_data is  None:
    start_quiz()

# Progress bar
progress_bar_value = (st.session_state.current_index + 1) / len(st.session_state.quiz_data)
st.metric(label="Score", value=f"{st.session_state.score} / {len(st.session_state.quiz_data) * 10}")
st.progress(progress_bar_value)

# Display the question and answer options
question_item = st.session_state.quiz_data[st.session_state.current_index]
st.subheader(f"Question {st.session_state.current_index + 1}")
st.subheader(f"{question_item['question']}")
# st.write(question_item['information'])

st.markdown(""" ___""")

# Answer selection
options = question_item['options']
correct_answer = question_item['answer']
explanantion =  question_item['explanation']


if st.session_state.answer_submitted:
    for i, option in enumerate(options):
        label = option
   
        if option == correct_answer:
            st.success(f"{label} (Correct answer)")
        elif option == st.session_state.selected_option:
            st.error(f"{label} (Incorrect answer)")
        else:
            st.write(label)
    st.toast( explanantion)
        # st.help( explanantion)
else:
    for i, option in enumerate(options):
        if st.button(option, key=i, use_container_width=True):
            st.session_state.selected_option = option

st.markdown(""" ___""")

# Submission button and response logic
if st.session_state.answer_submitted:
    if st.session_state.current_index < len(st.session_state.quiz_data) - 1:
        st.button('Next', on_click=next_question)
    else:
        st.write(f"Quiz completed! Your score is: {st.session_state.score} / {len(st.session_state.quiz_data) * 10}")
        if st.button('Restart', on_click=start_quiz):
            pass
else:
    if st.session_state.current_index < len(st.session_state.quiz_data):
        st.button('Submit', on_click=submit_answer)