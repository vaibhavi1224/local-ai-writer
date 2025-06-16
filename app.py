# app.py

import streamlit as st
import ollama
import datetime
import os

st.set_page_config(page_title="✍️ Local AI Writer", layout="centered")

# Title
st.title("✍️ Local AI Writer")
st.markdown("Generate creative blog intros using a **local LLM (LLaMA3)**. No cloud, no API.")

# Prompt input
prompt = st.text_area("Enter your blog topic or idea:", placeholder="e.g., The future of green energy in urban cities")

# Output box placeholder
output_placeholder = st.empty()

# Logs folder
os.makedirs("logs", exist_ok=True)
log_file = "logs/outputs.txt"

# Generate
if st.button("Generate Intro"):
    if prompt.strip() == "":
        st.warning("Please enter a topic to generate text.")
    else:
        with st.spinner("Generating with LLaMA3..."):
            response = ollama.chat(
                model='llama3',
                messages=[
                    {"role": "system", "content": "You are a creative AI assistant that writes catchy blog intros."},
                    {"role": "user", "content": f"Write a blog intro on: {prompt}"}
                ]
            )
            output = response['message']['content']
            output_placeholder.markdown(f"### 📝 Blog Intro:\n{output}")

            # Log output
            with open(log_file, "a") as f:
                f.write(f"\n---\n[{datetime.datetime.now()}]\nPrompt: {prompt}\nOutput:\n{output}\n")

            st.success("Output logged to logs/outputs.txt ✅")
