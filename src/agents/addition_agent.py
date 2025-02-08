import re
from .base_agent import BaseAgent
from .registry import register_agent

@register_agent
class AdditionAgent(BaseAgent):
    agent_name = "add"
    prompt_template = (
        "You are a calculator. Convert the following text into a simple addition expression. "
        "For example, 'one and two' becomes '1+2'. Input: {text}"
    )
    temperature = 0.0  # Deterministic output

    def process(self, text):
        prompt_text = self.prompt.format(text=text)
        # Use the LLM to generate an addition expression like "1+2"
        expr = self.llm(prompt_text).strip()
        # Use a regex to extract two numbers separated by '+'
        match = re.match(r'\s*(\d+)\s*\+\s*(\d+)\s*', expr)
        if match:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            result = num1 + num2
            return str(result)
        else:
            return f"Could not parse expression: {expr}"
