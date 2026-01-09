# boomer-vit-vellore-campus-assistant
An offline AI-powered campus assistant designed to help students navigate the VIT Vellore campus using natural language queries.
# 🎓 VIT Vellore Campus Assistant

An offline, AI-powered campus assistant that helps students navigate and understand the VIT Vellore campus using simple natural language queries.

This project is built as a **Level 1 AI Task**, focusing on core AI interaction without unnecessary complexity.

---

## ✨ Features

- Answers questions about VIT Vellore campus locations
- Gives directions (e.g., TT to SJT, Library, Hostels)
- Responds like a friendly senior student
- Works **offline**
- No API keys or paid services required

---

## 🧠 How It Works

1. User enters a question related to the VIT Vellore campus
2. The query is sent to a locally running language model using Ollama
3. The model generates a natural, human-like response
4. The response is displayed in the terminal

---

## 🛠️ Tech Stack

- Python
- Ollama (Local LLM Runtime)
- Mistral / LLaMA language model

---

## 🚀 Setup Instructions

### 1️⃣ Install Ollama
Download and install Ollama from:
https://ollama.com


Restart your system after installation.

---

### 2️⃣ Pull the Language Model
Open PowerShell or Terminal and run:
```bash
ollama pull mistral

Project Scope

This project is intentionally kept simple to demonstrate:

Basic AI interaction

Prompt-based behavior control

Offline inference using open-source models

Advanced features like databases, embeddings, or memory are outside the scope of Level 1.
