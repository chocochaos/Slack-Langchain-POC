from ..base_agent import BaseAgent
from ..registry import register_agent

@register_agent
class StoryAgent(BaseAgent):
    """Agent that generates user stories in markdown format."""

    def process(self, text):
        prompt_text = self.prompt.format(text=text)
        story = self.llm.invoke(prompt_text).content.strip()
        return f"```\n{story}\n```"
