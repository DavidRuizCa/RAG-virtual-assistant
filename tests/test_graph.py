from dotenv import load_dotenv
load_dotenv()

from rag_virtual_assistant.agent.graph import graph


def invoke_graph(user_message: str, thread_id: str) -> dict:
    config = {"configurable": {"thread_id": thread_id}}
    return graph.invoke({"messages": [{"role": "user", "content": user_message}]}, config)


def test_graph_returns_state():
    state = invoke_graph("Hello", "test-1")
    assert state is not None


def test_state_contains_messages():
    state = invoke_graph("Hello", "test-2")
    assert "messages" in state
    assert len(state["messages"]) > 0


def test_last_message_not_empty():
    state = invoke_graph("Hello", "test-3")
    last = state["messages"][-1]
    assert last.content is not None
    assert last.content.strip() != ""