from groq import Groq
import streamlit as st

GROQ_API_KEY = "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"

client = Groq(
    api_key = GROQ_API_KEY,
)

system_prompt = "Your task is to generate multiple proofread and correct of the given query."
query = st.text_input("Input here", placeholder = "Ask me!")

if query:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model="gemma-7b-it",
    )

    response = chat_completion.choices[0].message.content

    st.markdown(":blue[Query:]")
    st.markdown(query)
    st.markdown(":green[Response: ]")
    st.markdown(response)
