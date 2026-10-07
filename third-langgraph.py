from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph 

class Agentstate(TypedDict):
    name: str
    age: str
    skill: List[str]
    final: str

def First_node(state:Agentstate) -> Agentstate:
    '''This is the first node of our sequence'''

    state["final"] = f"Hi {state["name"]}! "
    return state

def Second_node(state:Agentstate) -> Agentstate:
    '''This is the second node of our sequence'''

    state["final"] = state["final"] + f"Your are  {state["age"]} years old!"
    return state

def Third_node(state:Agentstate) -> Agentstate:
    '''This is the third node to display the skills'''

    state["final"] = state['final'] + f"You have skills in: {",".join(state["skill"])}"
    return state

graph = StateGraph(Agentstate)
graph.add_node("First_node",First_node)
graph.add_node("Second_node",Second_node)
graph.add_node("Third_node",Third_node)
graph.set_entry_point("First_node")
graph.add_edge("First_node","Second_node")
graph.add_edge("Second_node","Third_node")
graph.set_finish_point("Third_node")
app = graph.compile()

result = app.invoke({"name":"charlie","age":20,"skill":["Python","Machine Learning","LangGraph"]})
print(result["final"])