from typing import Dict , TypedDict
from langgraph.graph import StateGraph, START, END


class Agentstate(TypedDict):
    number1: int
    operation: int
    number2: int
    finalNumber: int

def adder(state:Agentstate) -> Agentstate:
    ''' This node add two numbers'''

    state["finalNumber"] = state["number1"] + state["number2"]

    return state

def subtractor(state:Agentstate) -> Agentstate:
    '''This node subtractor the numbers'''
    state["finalNumber"] = state["number1"] - state["number2"]
    return state

def decide_next_node(state:Agentstate) -> Agentstate:
    '''This node will select the next node of the graph'''

    if state["operation"] == "+":
        return "addition_operation"
    elif state["operation"] == "-":
        return "subtraction_operation"


graph = StateGraph(Agentstate)
graph.add_node("add_node", adder)
graph.add_node("subtract_node", subtractor)
graph.add_node("router", lambda state:state)

graph.add_edge(START,"router")
graph.add_conditional_edges(
    "router",
    decide_next_node,
    {
        "addition_operation":"add_node",
        "subtraction_operation":"subtract_node"
    }
)

graph.add_edge("add_node",END)
graph.add_edge("subtract_node",END)

app = graph.compile()

initial_state_1 = Agentstate(number1 = 10, operation = "+", number2 = 5)
print(app.invoke(initial_state_1))