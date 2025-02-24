from ..base_agent import BaseAgent
from ..registry import register_agent

@register_agent
class EchoAgent(BaseAgent):
    """Agent that echoes back the input message."""

    def process(self, text):
        prompt_text = self.prompt.format(text=text)
        return self.llm.invoke(prompt_text).content
