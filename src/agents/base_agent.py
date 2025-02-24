import os
import sys
import yaml
from abc import ABC, abstractmethod
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

class BaseAgent(ABC):
    agent_name = None
    prompt_template = None
    temperature = 0.5

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Load configuration when a subclass is defined
        cls.load_config()

    @classmethod
    def load_config(cls):
        """Load agent configuration from YAML file."""
        module_path = sys.modules[cls.__module__].__file__
        agent_dir = os.path.dirname(module_path)
        config_path = os.path.join(agent_dir, 'config.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                # Set class variables from config
                cls.agent_name = config.get('agent_name', cls.agent_name)
                cls.prompt_template = config.get('prompt_template', cls.prompt_template)
                cls.temperature = config.get('temperature', cls.temperature)
                return config
        return {
            'agent_name': cls.agent_name,
            'prompt_template': cls.prompt_template,
            'temperature': cls.temperature
        }

    def __init__(self, openai_api_key):
        config = self.load_config()
        self.agent_name = config['agent_name']
        self.prompt_template = config['prompt_template']
        self.temperature = config['temperature']

        self.llm = OpenAI(api_key=openai_api_key, temperature=self.temperature)
        self.prompt = PromptTemplate(input_variables=["text"], template=self.prompt_template)

    @abstractmethod
    def process(self, text):
        pass
