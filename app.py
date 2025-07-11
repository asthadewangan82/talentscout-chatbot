import streamlit as st
import requests
import re

# 🧠 Ask local LLaMA2 model
def ask_llama2(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# 🌐 Page Config
st.set_page_config(page_title="TalentScout - AI Hiring Assistant", layout="centered")

# ⚠️ Data Privacy Disclaimer
st.info("\u26a0\ufe0f Your data is not stored or shared. All interactions are processed locally and deleted when you close the browser.")

# 🗓 Header UI
st.markdown("""
    <div style="text-align:center; padding: 10px 0;">
        <h1 style="color: #2E86AB;">TalentScout - AI Hiring Assistant</h1>
        <p style="color: #555;">Practice or conduct technical interviews using smart AI prompts.</p>
    </div>
    <hr style="margin-top: -10px;">
""", unsafe_allow_html=True)

# 🎨 Styled container for candidate form
st.markdown("""
    <div style="background-color: #f9f9f9; padding: 30px 25px; border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.05); margin-top: 20px;">
""", unsafe_allow_html=True)

st.markdown("### 👤 Candidate Information")

with st.form("candidate_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email (Optional)")
        experience = st.number_input("Years of Experience", min_value=0, step=1)

    with col2:
        phone = st.text_input("Phone Number (Optional)")
        location = st.text_input("Current Location")
        position = st.text_input("Desired Position")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### 💻 Tech Stack and Role")

    tech_stack = st.text_input("Your Tech Stack (e.g., Python, Django, OpenCV)")
    user_type = st.radio("I am a:", ["Job Seeker", "Interviewer"])
    submitted = st.form_submit_button("Start Interview")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- Session State Setup ----------
if "qa_mode" not in st.session_state:
    st.session_state.qa_mode = False
    st.session_state.questions = []
    st.session_state.current_q = 0
    st.session_state.ask_more = False
    st.session_state.show_feedback = False
    st.session_state.all_attempts = []

# ---------- After form is submitted ----------
if submitted:
    if not name or not tech_stack:
        st.warning("Please fill all required fields.")
    else:
        st.session_state.qa_mode = True
        st.session_state.questions = []
        st.session_state.current_q = 0
        st.session_state.ask_more = False
        st.session_state.show_feedback = False
        st.session_state.all_attempts = []

        prompt = (
            f"Generate 3 technical interview questions with answers for a {user_type.lower()} "
            f"having {experience} years of experience in {tech_stack}. "
            f"Format the response like:\nQ1. ...\nAnswer: ...\nQ2. ...\nAnswer: ..."
        )
        output = ask_llama2(prompt)

        qas = re.findall(r"Q\d+\.\s*(.*?)\nAnswer:\s*(.*?)(?=\nQ\d+\.|\Z)", output, re.DOTALL)
        st.session_state.questions = qas[:3]
        st.success("Interview started. Answer the questions one by one below ⬇️")

# ---------- One-by-One Q&A Flow ----------
if st.session_state.qa_mode and st.session_state.current_q < len(st.session_state.questions):
    q, correct_ans = st.session_state.questions[st.session_state.current_q]

    st.markdown(f"### ❓ Question {st.session_state.current_q + 1}:")
    st.markdown(f"**{q}**")

    user_ans = st.text_area("Your Answer:", key=f"user_ans_{st.session_state.current_q}")

    if st.button("Submit Answer", key=f"submit_btn_{st.session_state.current_q}"):
        st.session_state.all_attempts.append({
            "question": q.strip(),
            "user_answer": user_ans.strip(),
            "correct_answer": correct_ans.strip()
        })
        st.session_state.show_feedback = True

    if st.session_state.show_feedback:
        st.markdown("**Correct Answer:**")
        st.markdown(f"{correct_ans.strip()}")
        st.session_state.current_q += 1
        st.session_state.show_feedback = False
        st.rerun()

# ---------- Ask if more questions are needed ----------
elif st.session_state.qa_mode and not st.session_state.ask_more and st.session_state.current_q >= 3:
    st.markdown("---")
    st.markdown("You’ve completed 3 questions.")
    more = st.radio("Would you like to practice more questions?", ["Yes", "No"])

    if more == "Yes":
        prompt = (
            f"Generate 3 more technical interview questions with answers for a {user_type.lower()} "
            f"having {experience} years of experience in {tech_stack}."
        )
        output = ask_llama2(prompt)
        qas = re.findall(r"Q\d+\.\s*(.*?)\nAnswer:\s*(.*?)(?=\nQ\d+\.|\Z)", output, re.DOTALL)
        st.session_state.questions = qas[:3]
        st.session_state.current_q = 0
        st.session_state.qa_mode = True
        st.session_state.ask_more = False
        st.rerun()
    else:
        st.session_state.qa_mode = False
        st.markdown("---")
        st.markdown(
            f"""
            <div style="background-color: #e7f4e4; padding: 20px; border-radius: 10px;">
                <b>Thank you, {name}!</b><br>
                Your interview is complete. Here's a review of all questions and correct answers. 📑
            </div>
            """, unsafe_allow_html=True
        )

        for idx, qa in enumerate(st.session_state.all_attempts, 1):
            st.markdown(f"### 🔹 Question {idx}")
            st.markdown(f"**Q:** {qa['question']}")
            st.markdown(f"**Your Answer:** {qa['user_answer'] or '*No answer provided*'}")
            st.markdown(f"**Correct Answer:** {qa['correct_answer']}")
            st.markdown("---")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔁 Start Again"):
                st.session_state.qa_mode = False
                st.session_state.questions = []
                st.session_state.current_q = 0
                st.session_state.ask_more = False
                st.session_state.show_feedback = False
                st.session_state.all_attempts = []
                st.rerun()

        with col2:
            if st.button("➕ Continue Practicing"):
                prompt = (
                    f"Generate 3 more technical interview questions with answers for a {user_type.lower()} "
                    f"having {experience} years of experience in {tech_stack}."
                )
                output = ask_llama2(prompt)
                qas = re.findall(r"Q\d+\.\s*(.*?)\nAnswer:\s*(.*?)(?=\nQ\d+\.|\Z)", output, re.DOTALL)
                st.session_state.questions = qas[:3]
                st.session_state.current_q = 0
                st.session_state.qa_mode = True
                st.session_state.ask_more = False
                st.rerun()





