# ✅ `README.md`

# ✍️ Local AI Writer – Using Ollama & LLaMA3

This project is a lightweight AI writing app that runs **100% locally** using the LLaMA3 model and **Ollama** for inference. It helps generate blog introductions from a given topic—**without using OpenAI or cloud APIs**.


## ✅ App Type
**AI Writer** – Generates blog intros from a user-given topic.


## 🧠 Model Used
- **Model**: `llama3`  
- **Runtime**: Local via [Ollama](https://ollama.com)


## 🚀 Features

- Topic input prompt
- Local inference using LLaMA3 (no external API)
- Temperature control slider
- Output logging (saved in `logs/outputs.txt`)
- Simple Streamlit-based UI
- Lightweight and fast


## 🛠 How to Run Locally

### 1. Install [Ollama](https://ollama.com/download)
```bash
# Then pull the llama3 model:
ollama run llama3
````

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
local-ai-writer/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── logs/
│   └── outputs.txt         # Logged responses
└── README.md               # Project info
```

---

## 📝 Notes

* All model inference happens **locally** using Ollama.
* No keys or cloud dependencies required.
* Can be easily extended for Rephraser, Explainer, or Chatbot use-cases.
