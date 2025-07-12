# talentscout-chatbot
"AI-powered interview assistant that dynamically generates technical questions and provides smart feedback using local LLMs via Streamlit."
# TalentScout – AI Hiring Assistant Chatbot 🤖

This project is an AI-powered Hiring Assistant chatbot built for **TalentScout**, a fictional recruitment agency that specializes in tech placements. It assists in the initial candidate screening by collecting essential details and generating technical questions based on the declared tech stack. The bot supports both **Job Seekers** and **Interviewers**, offering a personalized one-on-one question-answer experience.

---

## 🔍 Features

- Interactive form to gather candidate or interviewer info
- Role selection: `Job Seeker` or `Interviewer`
- Intelligent prompt-driven technical questions generation
- One-on-one Q&A flow with follow-up questions
- Feedback-based logic: Ask more questions or end
- Shows correct answers if the candidate gives wrong or partial answers
- Restart option to begin a new session
- Locally runs with open-source LLMs like **LLaMA 2** or **Mistral** via Ollama

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io)
- **Backend LLM:** [Ollama](https://ollama.com/) (LLaMA 2 / Mistral)
- **Language:** Python
- **LLM Prompts:** Custom-crafted prompt logic for Q&A generation
- **Model Switchable:** Supports any local model via Ollama

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/asthadewangan82/talentscout-chatbot.git
cd talentscout-chatbot


---

````markdown
# TalentScout – AI Hiring Assistant Chatbot 🤖

This project is an AI-powered Hiring Assistant chatbot built for **TalentScout**, a fictional recruitment agency that specializes in tech placements. It assists in the initial candidate screening by collecting essential details and generating technical questions based on the declared tech stack. The bot supports both **Job Seekers** and **Interviewers**, offering a personalized one-on-one question-answer experience.

---

## 🔍 Features

- Interactive form to gather candidate or interviewer info
- Role selection: `Job Seeker` or `Interviewer`
- Intelligent prompt-driven technical questions generation
- One-on-one Q&A flow with follow-up questions
- Feedback-based logic: Ask more questions or end
- Shows correct answers if the candidate gives wrong or partial answers
- Restart option to begin a new session
- Locally runs with open-source LLMs like **LLaMA 2** or **Mistral** via Ollama

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io)
- **Backend LLM:** [Ollama](https://ollama.com/) (LLaMA 2 / Mistral)
- **Language:** Python
- **LLM Prompts:** Custom-crafted prompt logic for Q&A generation
- **Model Switchable:** Supports any local model via Ollama

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/asthadewangan82/talentscout-chatbot.git
cd talentscout-chatbot
````

2. **Create & activate virtual environment**

```bash
python -m venv .venv
.venv\Scripts\activate    # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Start local LLM server using Ollama**

```bash
ollama run llama2
# or
ollama run mistral
```

5. **Run Streamlit app**

```bash
streamlit run app.py
```

6. Open the app at `http://localhost:8501`

---

## 📁 File Structure

```
📦 talentscout-chatbot/
├── app.py                 # Main chatbot code
├── requirements.txt       # Python dependencies
├── README.md              # This file
```

---

## 🧠 Prompt Engineering

The chatbot dynamically crafts prompts to:

* Collect user inputs (name, experience, tech stack)
* Generate role-based technical questions
* Adjust conversation based on user type and feedback
* Offer retry logic and display correct answers if needed

---

## 🎯 Use Case Flows

1. **Job Seeker:**

   * Fills form → Answers technical Qs → Sees results → Chooses to continue or end

2. **Interviewer:**

   * Inputs own tech stack → Gets random questions for interview → Tests & evaluates candidate

---

## 📹 Demo

▶️ A demo recording has been provided (via Loom or screen capture).

---

## 🧪 Known Limitations

* Currently supports only local models via Ollama (not OpenAI API due to quota)
* No persistent database (session state only)
* No multilingual support or sentiment analysis yet

---

## ⚠️ Disclaimer

This is a prototype for educational purposes. Candidate data is not stored or shared. Ensure privacy compliance before production deployment.

---

## 📌 Future Improvements

* Streamlit Cloud Deployment
* Sentiment analysis during conversation
* Multilingual interaction
* Secure backend with encrypted storage
* Feedback metrics and analytics dashboard

---

## 🙋‍♀️ Created By

**Astha Dewangan**
Final-year Computer Science Student
Passionate about AI, Chatbots, and Prompt Engineering
[LinkedIn](https://linkedin.com/in/asthadewangan82) | [GitHub](https://github.com/asthadewangan82)

---

```

```
