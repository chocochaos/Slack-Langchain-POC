from .base_agent import BaseAgent
from .registry import register_agent

@register_agent
class EchoAgent(BaseAgent):
    agent_name = "echo"
    prompt_template = "Echo the following message: {text}"
    temperature = 0.5

    def process(self, text):
        prompt_text = self.prompt.format(text=text)
        return self.llm(prompt_text)
