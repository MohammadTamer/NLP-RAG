import os
import ollama

MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3")


def generate_answer(question: str, contexts: list):
    context_text = "\n".join(contexts)

    prompt = f"""
    You are an AI assistant specialized in answering questions based on provided documents.

    Instructions:
    - Use ONLY the provided context
    - If the answer is not in the context, say: "I don't know"
    - Be clear and concise
    - Do not hallucinate

    Context:
    {context_text}

    Question:
    {question}

    Answer:
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
