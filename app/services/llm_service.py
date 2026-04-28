import os
from abc import ABC, abstractmethod

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

class OpenAIProvider(LLMProvider):
    def __init__(self):
        import openai
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set in environment variables.")
        self.client = openai.OpenAI(api_key=self.api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

    def generate(self, prompt: str, system_message: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

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
        elif provider_name == "openai":
            return OpenAIProvider()
        elif provider_name == "gemini":
            return GeminiProvider()
        else:
            raise ValueError(f"Unsupported LLM provider: {provider_name}")


def generate_answer(question: str, contexts: list, provider_name: str = None, model_name: str = None):
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
    
    system_message = "أجب دائمًا باللغة العربية الفصحى."
    
    try:
        # Pass the provider_name from the user to the Factory
        provider = LLMFactory.get_provider(provider_name)
        
        # Override the model if the user specified one
        if model_name:
             if hasattr(provider, 'model'):
                 provider.model = model_name
             elif hasattr(provider, 'model_name'):
                 provider.model_name = model_name
             
        return provider.generate(prompt=prompt, system_message=system_message)

    except Exception as e:
        return f"حدث خطأ أثناء توليد الإجابة: {str(e)}"
