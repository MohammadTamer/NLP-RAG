import os
import ollama

MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")

client = ollama.Client(host=OLLAMA_HOST)

def generate_answer(question: str, contexts: list, model_name: str):
    context_text = "\n".join(contexts)
    model = model_name or MODEL_NAME
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
    try:
        response = client.chat(
            model=model,
            messages=[
                {"role": "system", "content": "أجب دائمًا باللغة العربية الفصحى."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]

    except Exception as e:
        return f"حدث خطأ أثناء توليد الإجابة: {str(e)}"
