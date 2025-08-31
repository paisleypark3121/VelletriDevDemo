import gradio as gr

def greet(name):
    return f"Ciao, {name}!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()