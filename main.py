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

app = App(token=SLACK_BOT_TOKEN)

template = "You are an assistant. Echo the following message: {text}"
prompt = PromptTemplate(input_variables=["text"], template=template)

llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.5)

@app.message("!echo")
def handle_echo(message, say):
    text = message.get("text", "")
    # Format the prompt with the user's text
    prompt_text = prompt.format(text=text)
    result = llm(prompt_text)
    say(result)

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
