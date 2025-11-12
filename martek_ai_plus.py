import streamlit as st
import openai

st.title("MARTEK AI+")

openai.api_key = st.secrets["OPENAI_API_KEY"]

user_text = st.text_area("Enter an email or message:")
if st.button("Generate my style of reply"):
    prompt = f"Reply naturally as MARTEK would — use his usual tone, grammar, and word choice. Message: {user_text}"
    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}],
    )
    st.write(response.choices[0].message["content"])
