from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
import requests

app = FastAPI()

API_KEY = "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"
API_URL = "https://huggingface.co/ibm%E2%80%91granite/granite%E2%80%913.2%E2%80%912b%E2%80%91instruct"

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SDLC Smart AI Assistance Model</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
  <style>
    html { scroll-behavior: smooth; }
    :root[data-theme="light"] {
      --bg: #fffaf0; --text: #222; --primary: #cc5500; --secondary: #f5deb3;
      --user-msg: #dcf8c6; --ai-msg: #fff1cc;
    }
    :root[data-theme="dark"] {
      --bg: #1e1e1e; --text: #f0f0f0; --primary: #cc5500; --secondary: #deb887;
      --user-msg: #005c4b; --ai-msg: #3e2f1c;
    }
    body {
      margin: 0; font-family: 'Poppins', sans-serif;
      background: var(--bg); color: var(--text);
      transition: all 0.3s ease-in-out;
      background-image: url('https://i.imgur.com/r2urzzX.png');
      background-repeat: no-repeat; background-position: center top 120px;
      background-size: 60%; background-attachment: fixed;
    }
    nav {
      background: var(--primary); padding: 1rem 2rem;
      display: flex; justify-content: space-between; align-items: center;
      position: sticky; top: 0; z-index: 999;
    }
    nav .logo { font-size: 1.5rem; color: white; font-weight: 700; }
    nav ul { list-style: none; display: flex; gap: 1.5rem; margin: 0; padding: 0; }
    nav ul li a { color: white; text-decoration: none; font-weight: 500; }
    nav ul li a:hover { text-decoration: underline; }
    .switch { position: relative; display: inline-block; width: 50px; height: 28px; }
    .switch input { opacity: 0; width: 0; height: 0; }
    .slider {
      position: absolute; cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #ccc; transition: .4s; border-radius: 34px;
    }
    .slider:before {
      position: absolute; content: "";
      height: 20px; width: 20px;
      left: 4px; bottom: 4px;
      background-color: white; transition: .4s; border-radius: 50%;
    }
    input:checked + .slider { background-color: #222; }
    input:checked + .slider:before { transform: translateX(22px); }

    header {
      background: var(--primary); text-align: center;
      padding: 2rem 1rem 1rem;
      color: white;
    }
    .title {
      font-size: 2.5rem; font-weight: 700; margin: 0;
      text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
    section {
      max-width: 800px; margin: 4rem auto;
      background: var(--secondary); padding: 1.5rem;
      border-radius: 12px; scroll-margin-top: 120px;
    }
    .section-title {
      font-size: 1.6rem; font-weight: 600; margin-bottom: 1rem;
    }
    .chat-container {
      background: var(--bg); padding: 1rem;
      border-radius: 14px; height: 500px;
      display: flex; flex-direction: column;
      box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }
    #chat-box {
      flex: 1; overflow-y: auto; padding: 1rem;
      border-radius: 10px; margin-bottom: 1rem;
      background: var(--secondary);
    }
    .msg {
      max-width: 70%; padding: 0.8rem 1rem;
      border-radius: 12px; margin: 0.5rem 0;
      line-height: 1.4; word-wrap: break-word;
    }
    .user-msg {
      background-color: var(--user-msg); align-self: flex-end;
      text-align: right;
    }
    .ai-msg {
      background-color: var(--ai-msg); align-self: flex-start;
      text-align: left;
    }
    form {
      display: flex; gap: 0.5rem;
    }
    textarea {
      flex: 1; padding: 0.8rem; font-size: 1rem;
      border-radius: 10px; border: 1px solid #ccc;
      resize: none; height: 60px;
    }
    button[type="submit"] {
      background-color: var(--primary); color: white;
      border: none; padding: 0.8rem 1.2rem;
      font-weight: 600; border-radius: 10px;
      cursor: pointer;
    }
    footer {
      text-align: center; padding: 2rem 1rem; font-size: 0.9rem;
    }
  </style>
</head>
<body>
  <nav>
    <div class="logo">SDLC AI</div>
    <ul>
      <li><a href="#home">Home</a></li>
      <li><a href="#chat">Chat</a></li>
      <li><a href="#features">Features</a></li>
      <li><a href="#how">How It Works</a></li>
      <li><a href="#about">About</a></li>
    </ul>
    <label class="switch">
      <input type="checkbox" id="theme-toggle">
      <span class="slider"></span>
    </label>
  </nav>

  <header id="home">
    <h1 class="title">SDLC Smart AI Assistance Model</h1>
  </header>

  <main>
    <section id="chat" class="chat-container">
      <div class="section-title">Chat with SDLC Smart AI</div>
      <div id="chat-box"></div>
      <form id="chat-form">
        <textarea id="message" required placeholder="Type your question..."></textarea>
        <button type="submit">Send</button>
      </form>
    </section>

    <section id="features">
      <div class="section-title">Key Features</div>
      <ul>
        <li>✅ Real-time SDLC knowledge base</li>
        <li>✅ Natural language understanding</li>
        <li>✅ Full SDLC coverage</li>
        <li>✅ Mobile-friendly dark/light mode</li>
      </ul>
    </section>

    <section id="how">
      <div class="section-title">How It Works</div>
      <ul>
        <li>💬 Ask any question about SDLC</li>
        <li>⚙️ AI analyzes and responds</li>
        <li>📘 Helpful guidance in seconds</li>
      </ul>
    </section>

    <section id="about">
      <div class="section-title">About the Assistant</div>
      <p>This AI model is your intelligent guide through the Software Development Life Cycle. Whether you're a student, developer, or project manager—it helps explain, recommend, and walk you through the entire SDLC process.</p>
    </section>
  </main>

  <footer>&copy; 2025 SDLC Smart AI | Built with FastAPI</footer>

  <script>
    const form = document.getElementById('chat-form');
    const messageBox = document.getElementById('message');
    const chatBox = document.getElementById('chat-box');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const msg = messageBox.value.trim();
      if (!msg) return;

      appendMessage(msg, "user-msg");
      messageBox.value = "";
      chatBox.scrollTop = chatBox.scrollHeight;

      appendMessage("AI is thinking...", "ai-msg", true);

      try {
        const res = await fetch("/chat", {
          method: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          body: new URLSearchParams({ message: msg })
        });
        const data = await res.json();
        removeTyping();
        appendMessage(data.reply, "ai-msg");
        chatBox.scrollTop = chatBox.scrollHeight;
      } catch {
        removeTyping();
        appendMessage("⚠️ Error: Could not reach AI.", "ai-msg");
      }
    });

    function appendMessage(text, cls, isTyping = false) {
      const msg = document.createElement("div");
      msg.className = `msg ${cls}`;
      msg.innerText = text;
      if (isTyping) msg.id = "typing-msg";
      chatBox.appendChild(msg);
    }

    function removeTyping() {
      const t = document.getElementById("typing-msg");
      if (t) t.remove();
    }

    const toggle = document.getElementById('theme-toggle');
    toggle.addEventListener('change', () => {
      const theme = toggle.checked ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
    });

    window.addEventListener('DOMContentLoaded', () => {
      const stored = localStorage.getItem('theme') || 'light';
      document.documentElement.setAttribute('data-theme', stored);
      document.getElementById('theme-toggle').checked = stored === 'dark';
    });
  </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=HTML_PAGE)

@app.post("/chat")
async def chat(message: str = Form(...)):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "IBM Granite 3.2‑2B‑Instruct",
        "messages": [{"role": "user", "content": message}]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return JSONResponse({"reply": reply})
    except Exception as e:
        return JSONResponse({"reply": f"Error: {str(e)}"})
