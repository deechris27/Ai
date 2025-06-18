from transformers import pipeline, set_seed
import gradio as gr


generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def generate_blog(topic, length):
    prompt = f"write a blog post about {topic}. \n\n"
    result = generator(prompt, max_length=int(length), num_return_sequences=1)[0]['generated_text']
    return result

gr.Interface(
    fn=generate_blog,
    inputs = [
        gr.Textbox(label="Topic", placeholder="e.g Benefits of meditation"),
        gr.Slider(50, 500, value=250, label="Set Blog length (words)")
    ],
    outputs="text",
    title="AI Article Writer",
    description="Enter a topic and let AI write you an article"
).launch(share=True)