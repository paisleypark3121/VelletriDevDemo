import os
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def chat_with_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

iface = gr.Interface(
    fn=chat_with_llm,
    inputs="text",
    outputs="text",
    title="Chat con LLM via OpenAI API"
)

iface.launch()
