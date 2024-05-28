from groq import Groq
import streamlit as st
from redlines import Redlines
from IPython.display import display, Markdown

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
    diff = Redlines(query, response)
    

    st.markdown(":blue[Query:]")
    st.markdown(query)
    st.markdown(":green[Response: ]")
    st.markdown(diff.output_markdown, unsafe_allow_html = True)
