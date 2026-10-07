from typing import Dict , TypedDict, List 
from langgraph.graph import StateGraph
import math


class Agentstate(TypedDict):
    values: List[int]
    name: str
    operation: str
    result: str

def process_values(state:Agentstate) -> Agentstate:
    '''This function handles multiple diffrent inputs'''
    if state["operation"] == "*":
         state["result"] = f"Hi there{state["name"]}! Your product = {math.prod(state["values"])}"
    elif state["operation"] == "+":
        state["result"] = f"Hi there{state["name"]}! Your sum = {sum(state["values"])}"
    return state

graph = StateGraph(Agentstate)
graph.add_node("processor",process_values)
graph.set_entry_point("processor")
graph.set_finish_point("processor")
app = graph.compile()

result = app.invoke({"values": [1,2,3,4], "name":"Steve","operation":"*"})
print(result["result"])