from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import gradio as gr
import torch


model_id = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16,
)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_blog(topic, length):
    prompt = f"Write a detailed blog article about: {topic}\n\n"
    output = pipe(prompt, max_new_tokens=int(length), do_sample=True, temperature=0.7)[0]["generated_text"]
    return output

gr.Interface(
    fn=generate_blog,
    inputs=[
        gr.Textbox(label="Topic", placeholder="e.g Rise of remote work"),
        gr.Slider(50, 400, value=200, label="Set Blog length (words)")
    ],
    outputs="text",
    title="LLama blog generator",
    description="Generate a detailed blog post using the LLama 2 7B model"
).launch()