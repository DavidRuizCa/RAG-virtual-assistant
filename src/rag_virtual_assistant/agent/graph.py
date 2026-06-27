from openai import OpenAI
from langgraph.graph import StateGraph, START, END
from rag_virtual_assistant.agent.state import State
from rag_virtual_assistant.config import Settings

settings = Settings()
client = OpenAI(api_key=settings.openai_api_key.get_secret_value())

def call_model(state: State) -> dict:
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages = [{"role": m.type if m.type != "human"
        else "user", "content": m.content} for m in state["messages"]]
    )
    content = response.choices[0].message.content
    return {"messages": [{"role": "assistant", "content": content}]}

# 2. Construye el grafo
builder = StateGraph(State)
builder.add_node("call_model", call_model)
builder.add_edge(START, "call_model")
builder.add_edge("call_model", END)

# 3. Compila
graph = builder.compile()