from abc import ABC, abstractmethod
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

class BaseAgent(ABC):
    agent_name = None
    prompt_template = None
    temperature = 0.5

    def __init__(self, openai_api_key):
        self.llm = OpenAI(api_key=openai_api_key, temperature=self.temperature)
        self.prompt = PromptTemplate(input_variables=["text"], template=self.prompt_template)

    @abstractmethod
    def process(self, text):
        pass
