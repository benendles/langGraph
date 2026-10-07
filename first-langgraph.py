from typing import Dict , TypedDict
from langgraph.graph import StateGraph 

class Agentstate(TypedDict):
    name : str

def greeting_node(state:Agentstate) -> Agentstate:
    ''' Simple node that add a greeting message to the state '''

    state['name'] = "Hey " + state["name"] + ", you're doing an amazing job learning LangGraph"

    return state

graph = StateGraph(Agentstate)

graph.add_node("greeter",greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result = app.invoke({"name":"Bob"})

print(result["name"])