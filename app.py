import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(page_title="Groq Q&A Chatbot", page_icon="💬", layout="wide")

# ----------------------------
# Secrets / API key
# ----------------------------
groq_api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))
if not groq_api_key:
    st.error("GROQ_API_KEY not found. Add it in Streamlit Cloud → Settings → Secrets.")
    st.stop()

GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# ----------------------------
# LangChain prompt + parser
# ----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer clearly, politely, and accurately."),
        ("user", "Question: {question}"),
    ]
)
parser = StrOutputParser()

# ----------------------------
# Styling (CSS)
# ----------------------------
def inject_css():
    st.markdown(
        """
        <style>
        /* Global */
        .block-container { padding-top: 2rem; padding-bottom: 2.5rem; max-width: 1200px; }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, rgba(20,20,35,0.95), rgba(10,10,18,0.95)); }
        [data-testid="stSidebar"] * { color: #f3f4f6 !important; }
        .stApp { background: radial-gradient(1200px 800px at 15% 10%, rgba(99,102,241,0.25), transparent 60%),
                        radial-gradient(1000px 700px at 85% 20%, rgba(16,185,129,0.18), transparent 55%),
                        linear-gradient(180deg, #070712 0%, #06060f 50%, #05050c 100%); }

        /* Hide Streamlit menu/footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Hero card */
        .hero {
            border-radius: 22px;
            padding: 42px 36px;
            background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.03));
            border: 1px solid rgba(255,255,255,0.12);
            box-shadow: 0 18px 50px rgba(0,0,0,0.35);
            backdrop-filter: blur(10px);
        }
        .hero h1 {
            font-size: 46px; line-height: 1.05; margin: 0;
            color: #ffffff; letter-spacing: -0.02em;
        }
        .hero p {
            margin-top: 14px;
            font-size: 16px;
            color: rgba(255,255,255,0.78);
            max-width: 760px;
        }
        .badge-row { margin-top: 18px; display: flex; gap: 10px; flex-wrap: wrap; }
        .badge {
            padding: 7px 12px;
            border-radius: 999px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.10);
            color: rgba(255,255,255,0.86);
            font-size: 13px;
        }

        /* Section cards */
        .card {
            border-radius: 18px;
            padding: 22px 20px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.10);
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        }
        .card h3 { margin: 0 0 8px 0; color: #fff; font-size: 18px; }
        .card p { margin: 0; color: rgba(255,255,255,0.75); font-size: 14px; line-height: 1.55; }

        /* Primary button styling */
        div.stButton > button {
            border-radius: 14px;
            padding: 12px 16px;
            border: 1px solid rgba(255,255,255,0.18);
            background: linear-gradient(135deg, rgba(99,102,241,0.95), rgba(16,185,129,0.85));
            color: white;
            font-weight: 700;
            box-shadow: 0 10px 25px rgba(0,0,0,0.25);
        }
        div.stButton > button:hover {
            transform: translateY(-1px);
            filter: brightness(1.04);
        }

        /* Chat bubble styling */
        .chat-wrap {
            border-radius: 18px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.10);
            padding: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.22);
        }

        /* Small helper text */
        .muted { color: rgba(255,255,255,0.65); font-size: 13px; }

        </style>
        """,
        unsafe_allow_html=True,
    )

inject_css()

# ----------------------------
# State init
# ----------------------------
if "page" not in st.session_state:
    st.session_state.page = "landing"  # landing -> setup -> chat

if "settings" not in st.session_state:
    st.session_state.settings = {
        "model": "llama-3.1-8b-instant",
        "temperature": 0.7,
        "max_tokens": 512,
    }

if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {"role": "user"/"assistant", "content": str}


# ----------------------------
# LLM call
# ----------------------------
def generate_response(question: str) -> str:
    cfg = st.session_state.settings
    llm = ChatOpenAI(
        api_key=groq_api_key,
        base_url=GROQ_BASE_URL,
        model=cfg["model"],
        temperature=cfg["temperature"],
        max_tokens=cfg["max_tokens"],
    )
    chain = prompt | llm | parser
    return chain.invoke({"question": question})


# ----------------------------
# Navigation helpers
# ----------------------------
def go(page_name: str):
    st.session_state.page = page_name
    st.rerun()


# ----------------------------
# Landing Page
# ----------------------------
def landing_page():
    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown(
            """
            <div class="hero">
              <h1>Groq-Powered Q&A Chatbot</h1>
              <p>
                A clean, fast, and modern chatbot built with <b>Streamlit</b> + <b>LangChain</b>,
                running online on <b>Streamlit Community Cloud</b> and powered by the <b>Groq</b> API.
                Choose a model, tune generation settings, and chat in a simple interface.
              </p>
              <div class="badge-row">
                <span class="badge">⚡ Fast responses</span>
                <span class="badge">☁️ Runs online (Free)</span>
                <span class="badge">🔐 Secure secrets</span>
                <span class="badge">🧠 Multiple models</span>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        cta1, cta2 = st.columns([1, 1])
        with cta1:
            if st.button("🚀 Get Started"):
                go("setup")
        with cta2:
            if st.button("💬 Go to Chat"):
                go("chat")

    with col2:
        st.markdown(
            """
            <div class="card">
              <h3>How it works</h3>
              <p>
                1) Start on this landing page<br/>
                2) Configure model + parameters<br/>
                3) Chat with a friendly UI
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            """
            <div class="card">
              <h3>Made for</h3>
              <p>
                Students, demos, portfolios, mini projects, and quick Q&A tools.
                Deploy from GitHub and share a link with anyone.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ----------------------------
# Setup Page
# ----------------------------
def setup_page():
    st.markdown(
        """
        <div class="hero">
          <h1>Setup</h1>
          <p>Choose your model and generation settings. You can change these later anytime.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    left, right = st.columns([1, 1])

    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Model")
        model = st.selectbox(
            "Select Groq model",
            ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "gemma2-9b-it"],
            index=["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "gemma2-9b-it"].index(
                st.session_state.settings["model"]
            ),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Generation controls")
        temperature = st.slider("Temperature", 0.0, 1.0, float(st.session_state.settings["temperature"]), 0.05)
        max_tokens = st.slider("Max tokens", 64, 2048, int(st.session_state.settings["max_tokens"]), 64)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    action1, action2, action3 = st.columns([1, 1, 1])
    with action1:
        if st.button("⬅️ Back"):
            go("landing")
    with action2:
        if st.button("💾 Save Settings"):
            st.session_state.settings["model"] = model
            st.session_state.settings["temperature"] = float(temperature)
            st.session_state.settings["max_tokens"] = int(max_tokens)
            st.success("Saved! Now you can start chatting.")
    with action3:
        if st.button("➡️ Continue to Chat"):
            st.session_state.settings["model"] = model
            st.session_state.settings["temperature"] = float(temperature)
            st.session_state.settings["max_tokens"] = int(max_tokens)
            go("chat")


# ----------------------------
# Chat Page
# ----------------------------
def chat_page():
    # Sidebar (always available on chat page)
    st.sidebar.header("Chat Controls")
    st.sidebar.caption("Adjust anytime. Changes apply to new messages.")

    st.session_state.settings["model"] = st.sidebar.selectbox(
        "Model",
        ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "gemma2-9b-it"],
        index=["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "gemma2-9b-it"].index(
            st.session_state.settings["model"]
        ),
    )
    st.session_state.settings["temperature"] = st.sidebar.slider(
        "Temperature", 0.0, 1.0, float(st.session_state.settings["temperature"]), 0.05
    )
    st.session_state.settings["max_tokens"] = st.sidebar.slider(
        "Max tokens", 64, 2048, int(st.session_state.settings["max_tokens"]), 64
    )

    if st.sidebar.button("🧹 Clear chat"):
        st.session_state.messages = []
        st.rerun()

    st.sidebar.divider()
    if st.sidebar.button("🏠 Home"):
        go("landing")
    if st.sidebar.button("⚙️ Setup"):
        go("setup")

    st.markdown(
        """
        <div class="hero">
          <h1>Chat</h1>
          <p class="muted">Ask anything. Your chat history stays in this session.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

    # Show history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input
    user_text = st.chat_input("Type your message...")

    if user_text:
        # Store user message
        st.session_state.messages.append({"role": "user", "content": user_text})
        with st.chat_message("user"):
            st.markdown(user_text)

        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("Generating..."):
                try:
                    answer = generate_response(user_text)
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# Router
# ----------------------------
if st.session_state.page == "landing":
    landing_page()
elif st.session_state.page == "setup":
    setup_page()
else:
    chat_page()
