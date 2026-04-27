import os
import ollama

MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")

client = ollama.Client(host=OLLAMA_HOST)

def generate_answer(question: str, contexts: list):
    context_text = "\n".join(contexts)

    prompt = f"""
    أنت مساعد ذكي متخصص في شرح النصوص القانونية.

    تعليمات:
    - أجب باللغة العربية الفصحى.
    - اعتمد على المعلومات المقدمة.
    - يمكنك إعادة صياغة المعلومات وشرحها بشكل واضح.
    - لا تخترع معلومات غير موجودة.
    - إذا لم تجد الإجابة بوضوح، قل: "لا توجد معلومات كافية."

    السؤال:
    {question}

    المعلومات:
    {context_text}

    الإجابة:
    """

    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
