import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import google.generativeai

load_dotenv(override=True)

gemini_api_key = os.getenv('GOOGLE_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

if not gemini_api_key:
    print('No API key found')
else:
    print('Valid Gemini API found!')
if not openai_api_key:
    print('No API key found')
else:
    print('Valid OpenAI api key found')

google.generativeai.configure()

openai = OpenAI()

system_prompt = "You are a smart assistant for an Airline called Mytidbit Airlines"
system_prompt += "You provide courteous answers and suggest the right alternative source for the info if you don't have the requested information"

ticket_prices = {"Berlin": "$899", "Chennai": "$599", "Okinawa": "$799", "Nancy": "$789", "Bangkok": "$699"}

def get_ticket_price(city):
     destination_city = city.lower()
     return ticket_prices.get(destination_city, "Unknown")

price_function = {
    "name": "price_function",
    "description": "Get the price of the requested tavel destination city. Call this whenever a customer asks like 'How much is the cost of ticket for Paris or Tokyo etc'",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city":{
                "type": "string",
                "description": "The city customer wants to travel to"
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function": price_function}]

def handle_tool_call(message):
   tool_call = message.tool_calls[0]
   arguments = json.loads(tool_call.function.arguments)
   city = arguments.get("destination_city")
   price = get_ticket_price(city)
   response = {
       "role": "tool",
       "content": json.dumps({"destination_city": city, "price": price}),
       "tool_call_id": tool_call.id
   }
   return response, city

def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model='gpt-4o-mini', messages=message, tools=tools)
    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content

gr.ChatInterface(fn=chat, type="messages").launch()