import re
from ..base_agent import BaseAgent
from ..registry import register_agent

@register_agent
class AdditionAgent(BaseAgent):
    """Agent that handles addition operations."""

    def process(self, text):
        prompt_text = self.prompt.format(text=text)
        # Use the LLM to generate an addition expression like "1+2"
        expr = self.llm.invoke(prompt_text).content.strip()
        # Use a regex to extract two numbers separated by '+'
        match = re.match(r'\s*(\d+)\s*\+\s*(\d+)\s*', expr)
        if match:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            result = num1 + num2
            return str(result)
        else:
            return f"Could not parse expression: {expr}"
