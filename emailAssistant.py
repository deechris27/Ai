from transformers import pipeline, set_seed
import gradio as gr

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_email(intent, tone):
    prompt = f"write a {tone.lower()} email for this situation: \n{intent}\n\nEmail:\n"
    result = generator(prompt, max_length=150, num_return_sequences=1)[0]["generated_text"]
    return result

gr.Interface(
    fn=generate_email,
    inputs=[
        gr.Textbox(label="Email Intent", placeholder="e.g Reschedule meeting with client to Friday"),
        gr.Radio(["Formal", "Casual"], label="Tone", value="formal")
    ],
    outputs="text",
    title="AI Email Assistant",
    description="Describe what you want to say, chose a tone, let AI draft the email!"
).launch()