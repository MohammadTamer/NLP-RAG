import os
from abc import ABC, abstractmethod
import ollama

MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")

client = ollama.Client(host=OLLAMA_HOST)

class LLMProvider(ABC):
    """Abstract Base Class for LLM Providers."""
    @abstractmethod
    def generate(self, prompt: str, system_message: str) -> str:
        pass


class OllamaProvider(LLMProvider):
    def __init__(self):
        import ollama
        self.host = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")
        self.model = os.getenv("OLLAMA_MODEL", "llama3")
        self.client = ollama.Client(host=self.host)

    def generate(self, prompt: str, system_message: str) -> str:
        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]


class GeminiProvider(LLMProvider):
    def __init__(self):
        import google.generativeai as genai
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set in environment variables.")
        genai.configure(api_key=self.api_key)
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
        self.model = genai.GenerativeModel(self.model_name)
        
    def generate(self, prompt: str, system_message: str) -> str:
        full_prompt = f"System: {system_message}\n\nUser: {prompt}"
        response = self.model.generate_content(full_prompt)
        return response.text

class LLMFactory:
    """Factory to instantiate the appropriate LLM provider."""
    @staticmethod
    def get_provider(provider_name: str = None) -> LLMProvider:
        if provider_name is None:
            provider_name = os.getenv("LLM_PROVIDER", "ollama").lower()
            
        if provider_name == "ollama":
            return OllamaProvider()
        elif provider_name == "gemini":
            return GeminiProvider()
        else:
            raise ValueError(f"Unsupported LLM provider: {provider_name}")


def generate_answer(question: str, contexts: list, provider_name: str = None, model_name: str = None):
    context_text = "\n".join(contexts)

    system_message = """
You are an AI assistant specialized in question answering using provided documents only.

Rules:
- Answer ONLY from the given context.
- Do NOT use external knowledge.
- If the answer is not found in the context, reply exactly with:
  "I don't know"
- Be accurate, concise, and clear.
- Do not hallucinate or make assumptions.
- If the context contains multiple relevant pieces of information, combine them naturally.
- Keep the answer professional and easy to understand.
"""

    prompt = f"""
Context:
{context_text}

Question:
{question}

Answer:
"""

    try:
        provider = LLMFactory.get_provider(provider_name)

        if model_name:
            if hasattr(provider, 'model'):
                provider.model = model_name
            elif hasattr(provider, 'model_name'):
                provider.model_name = model_name

        return provider.generate(
            prompt=prompt,
            system_message=system_message
        )

    except Exception as e:
        return f"An error occurred while generating the answer: {str(e)}"