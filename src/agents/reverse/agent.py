from ..base_agent import BaseAgent
from ..registry import register_agent

@register_agent
class ReverseAgent(BaseAgent):
    """Agent that reverses the order of words in the input message."""

    def process(self, text):
        prompt_text = self.prompt.format(text=text)
        return self.llm(prompt_text)
