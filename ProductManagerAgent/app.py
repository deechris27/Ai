import os
import json
from dotenv import load_dotenv
from memory import add_product, update_product, delete_product, list_products

from langgraph.graph import StateGraph, END
from langchain.schema import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Optional

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.4)


class ProductState(TypedDict, total=False):
    name: str
    price: float
    action: str

def parse_intent(state):
    user_input = state.get("input")
    if not user_input:
        return ProductState(**state, parsed="{}")

    system_prompt = """You are an intent parser for a Product Manager assistant.
    Extract the following from user input:
    - action (add, update, delete, list)
    - product_name
    - price (if applicable)

    Respond ONLY in this JSON format:
    {"action": "add|update|delete|list", "product_name": "string or null", "price": number or null}
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    parsed = llm(messages).content
    
    return ProductState(**state, product=parsed)

def execute_action(state):
    parsed = json.loads(state.get("parsed", "{}"))
    action = parsed.get("action")
    name = parsed.get("name")
    price = parsed.get("price")

    if action == "add":
        result = add_product(name, price)
    elif action == "update":
        result = update_product(name, price)
    elif action == "delete":
        result = delete_product(name)
    elif action == "list":
        result = list_products()
    else:
        result = "Unknown action"

        # new_state = dict(state)
        # new_state["result"] = result

        return ProductState(**state, result=result)

graph = StateGraph(ProductState)
graph.add_node("ParseIntent", parse_intent)
graph.add_node("ExecuteAction", execute_action)

graph.set_entry_point("ParseIntent")
graph.add_edge("ParseIntent", "ExecuteAction")
graph.add_edge("ExecuteAction", END)

app = graph.compile()

if __name__ == "__main__":
    print("Gemini product manager agent ready")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = app.invoke(ProductState(input=user_input))
        print(" Raw result:", result)

        #print("Bot :", result["result"])
