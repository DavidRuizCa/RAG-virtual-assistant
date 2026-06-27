from dotenv import load_dotenv
load_dotenv()

from rag_virtual_assistant.agent.graph import graph

def test_graph(user_message: str, thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    answer = graph.invoke({"messages": [{"role": "user", "content": user_message}]}, config)
    return answer["messages"][-1].content

print(test_graph("Mi nombre es Juan", "conversacion-1"))
print(test_graph("¿Cuál es mi nombre?", "conversacion-1"))