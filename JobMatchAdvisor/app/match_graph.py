from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.match_agent import compare_resume_to_job


class MatchState(TypedDict, total=False):
    resume: str
    job: str
    match_summary: str

def run_match(resume: str, job: str):
    graph = StateGraph(MatchState)

    def analyze(state: MatchState):
        print("Incoming state:", state)
        summary = compare_resume_to_job(state["resume"], state["job"])
        print("Claude response:", summary)
        return MatchState(**state, match_summary=summary)

    graph.add_node("MatchAnalyzer", analyze)
    graph.set_entry_point("MatchAnalyzer")
    graph.add_edge("MatchAnalyzer", END)

    app = graph.compile().with_config({"recall_all": True})
    result = app.invoke(MatchState(resume=resume, job=job))

    print("Final state:", result)
    return result.get("match_summary") if isinstance(result, dict) else {"error": "No result"}
