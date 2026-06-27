from dotenv import load_dotenv
load_dotenv()

from rag_virtual_assistant.agent.graph import graph

def test_graph(user_message: str):
    answer = graph.invoke({"messages": [{"role": "user", "content": user_message}]})
    return answer["messages"][-1].content

print(test_graph("Hola, ¿cómo estás?"))