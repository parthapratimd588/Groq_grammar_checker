from groq import Groq
import streamlit as st

GROQ_API_KEY = "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"

client = Groq(
    api_key = GROQ_API_KEY,
)

system_prompt = f""" 
Given a paragraph as query, your duty  is to check grammatical error in each sentence, and return all correct words in green color and all wrong color in red color with a horizonal red line cut over the wrong words. Don't do anything else.
"""
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