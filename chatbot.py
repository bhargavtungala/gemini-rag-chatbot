from langchain.schema import HumanMessage, AIMessage
from langchain_google_vertexai import ChatVertexAI
from rag_utils import retrieve_similar

MODEL_ID = "gemini-2.5-flash-preview-05-20"
llm = ChatVertexAI(model=MODEL_ID, temperature=0.7)

conversation_history = []

def generate_response(user_input):
    conversation_history.append({"role": "user", "content": user_input})

    messages = []
    for turn in conversation_history[-5:]:
        if turn["role"] == "user":
            messages.append(HumanMessage(content=turn["content"]))
        else:
            messages.append(AIMessage(content=turn["content"]))

    # Add context from vector store (RAG)
    context_docs = retrieve_similar(user_input)
    context_str = "\n".join(context_docs)
    messages.insert(0, HumanMessage(content=f"Use the following context:\n{context_str}"))

    response = llm(messages).content
    conversation_history.append({"role": "assistant", "content": response})
    return response
