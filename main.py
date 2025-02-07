import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

slack = App(token=SLACK_BOT_TOKEN)
open_ai = OpenAI(api_key=OPENAI_API_KEY, temperature=0.5)

echo_template = "Echo the following message: {text}"
echo_prompt = PromptTemplate(input_variables=["text"], template=echo_template)

@slack.message("!echo")
def handle_echo(message, say):
    user_message = message.get("text", "")
    promp_text = echo_prompt.format(text=user_message)
    agent_response = open_ai(promp_text)
    say(agent_response)

reverse_template = "Reverse the order of words in the following message. Be sure not to skip any words after this: {text}"
reverse_prompt = PromptTemplate(input_variables=["text"], template=reverse_template)

@slack.message("!reverse")
def handle_reverse(message, say):
    user_message = message.get("text", "")
    prompt_text = reverse_prompt.format(text=user_message)
    agent_response = open_ai(prompt_text)
    say(agent_response)

if __name__ == "__main__":
    handler = SocketModeHandler(slack, SLACK_APP_TOKEN)
    handler.start()
