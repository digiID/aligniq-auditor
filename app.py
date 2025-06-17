import openai
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AlignIQ – Truth & Bias Auditor")
st.title("🔍 AlignIQ: LLM Truth & Bias Auditor")
st.markdown("Enter AI output to analyze **truth**, **bias**, and **risk**.")

input_text = st.text_area("Paste LLM Output Here", height=200)

if st.button("Run Audit") and input_text:
    with st.spinner("Auditing with GPT-4..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI ethics and compliance auditor. Analyze the user's input for factual accuracy, political bias, and risk of harm. Respond in clear bullet points."},
                    {"role": "user", "content": input_text}
                ],
                temperature=0.2
            )
            result = response.choices[0].message.content
            st.success("✅ Audit Complete")
            st.markdown(result)
        except Exception as e:
            st.error(f"Audit failed: {e}")

