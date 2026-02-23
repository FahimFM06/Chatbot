💬 Groq-Powered Q&A Chatbot

A Multi-Page Streamlit Chat Application Using LangChain and Groq API

🔗 Live App:
https://chatbot-cdb8appvfzeedfhbbwgxw2v.streamlit.app/

📌 Project Overview

This project is a modern multi-page Q&A chatbot built using:

Streamlit (for the web interface)

LangChain (for model interaction handling)

Groq API (for fast LLM inference)

GitHub + Streamlit Community Cloud (for free deployment)

The chatbot allows users to:

Select different Groq models

Adjust temperature and max tokens

Chat in a clean, modern UI

Navigate between landing, setup, and chat pages

Run fully online without local installation

This project is designed for:

Educational purposes

Portfolio demonstrations

Research experiments with LLM APIs

Beginners learning Streamlit deployment

🏗️ Project Structure
Q&A Chatbot/
│
├── app.py
├── requirements.txt
├── assets/
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
└── README.md
Folder Explanation

app.py → Main Streamlit application

requirements.txt → Python dependencies

assets/ → Background images used for different pages

README.md → Project documentation

⚙️ Technologies Used
Technology	Purpose
Streamlit	Frontend web app
LangChain	LLM integration
Groq API	Model inference
Python	Backend logic
GitHub	Version control
Streamlit Cloud	Free hosting
🚀 How the Application Works

The application contains three main pages:

1️⃣ Landing Page

Displays project introduction

Shows features and badges

Allows navigation to Setup or Chat

2️⃣ Setup Page

User selects:

Model

Temperature

Max Tokens

Settings are stored in session state

3️⃣ Chat Page

User sends a message

Message is passed to Groq model via LangChain

Response is displayed

Chat history is stored for the session

🧠 Supported Models (Groq)

Currently supported and stable models:

llama-3.1-8b-instant

llama-3.3-70b-versatile

groq/compound-mini

groq/compound

Note: Some models (like gemma2-9b-it) were deprecated by Groq and are no longer supported.

🔐 API Key Setup

This project uses a Groq API key stored securely in Streamlit Secrets.

Step 1: Generate API Key

Go to: https://console.groq.com/

Create an account (if needed)

Navigate to API Keys

Generate a new key

Step 2: Add API Key to Streamlit Cloud

In Streamlit Cloud:

Open your app

Click Settings → Secrets

Add:

GROQ_API_KEY = "your_groq_api_key_here"

Click Save

Restart the app

🖥️ How to Run Locally

If someone wants to run this project locally:

Step 1: Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd "Q&A Chatbot"
Step 2: Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Set Environment Variable

Windows:

set GROQ_API_KEY=your_key_here

Mac/Linux:

export GROQ_API_KEY=your_key_here

Or create a .env file:

GROQ_API_KEY=your_key_here
Step 5: Run the App
streamlit run app.py
☁️ How Deployment Works (GitHub → Streamlit Cloud)

Code is pushed to GitHub

Streamlit Cloud connects to repository

requirements.txt installs dependencies

app.py runs automatically

Secrets are injected securely

App becomes publicly available

Every time new code is pushed:

The app automatically redeploys

🎨 UI Features

Glassmorphism panels

Custom neon background images

Multi-page navigation

Sidebar controls

Session-based chat memory

Responsive layout
