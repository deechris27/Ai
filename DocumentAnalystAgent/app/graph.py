from langgraph.graph import StateGraph, END
from app.agents import extract_summary_from_text
import pdfplumber
import io
from typing import TypedDict, Optional

class SummaryState(TypedDict, total=False):
    filename: str
    text: str
    summary: dict

def run_graph(filename: str, content: bytes):
    # Extract raw text here (outside LangGraph)
    with pdfplumber.open(io.BytesIO(content)) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    graph = StateGraph(SummaryState)

    #LangGraph only processes `text`, not bytes
    def parse_and_extract(state):
        print("📥 Received state in node:", state)

        text = state.get("text")
        if not text:
            print("No text found in state!")
            return SummaryState(**state, summary={"error": "No text in input"})

        try:
         parsed = extract_summary_from_text(text)
         print("Parsed summary:", parsed)
         return SummaryState(**state, summary=parsed)
        except Exception as e:
          print("[ERROR in parse_and_extract]:", e)
          return SummaryState(**state, summary={"error": str(e)})


    graph.add_node("Extract", parse_and_extract)
    graph.set_entry_point("Extract")
    graph.add_edge("Extract", END)

    app = graph.compile()
    app = app.with_config({"recall_all": True})
    initial_state = SummaryState(filename=filename, text=text)
    result = app.invoke(initial_state)
 
    print("LangGraph final state:", result)
    if isinstance(result, dict):
        return result.get("summary", {})
    else:
        return {"error": "LangGraph returned None or invalid"}
