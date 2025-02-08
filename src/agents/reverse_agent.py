from .base_agent import BaseAgent
from .registry import register_agent

@register_agent
class ReverseAgent(BaseAgent):
    agent_name = "reverse"
    prompt_template = "Reverse the order of words in the following message. Be sure not to skip any words after this: {text}"
    temperature = 0.2

    def process(self, text):
        prompt_text = self.prompt.format(text=text)
        return self.llm(prompt_text)
