import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from agents.registry import AGENT_REGISTRY
from functools import partial

load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

slack = App(token=SLACK_BOT_TOKEN)
agent_registry = {name: cls(OPENAI_API_KEY) for name, cls in AGENT_REGISTRY.items()}

def handle_agent_message(agent, slack_trigger, message, say):
    text = message.get("text", "")
    if slack_trigger in text:
        result = agent.process(text)
        say(result)

for agent_name, agent in agent_registry.items():
    slack_trigger = "!" + agent_name
    slack.message(slack_trigger)(partial(handle_agent_message, agent, slack_trigger))

if __name__ == "__main__":
    handler = SocketModeHandler(slack, SLACK_APP_TOKEN)
    handler.start()
