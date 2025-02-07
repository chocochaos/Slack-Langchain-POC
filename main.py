import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

# Load environment variables from your .env file
load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Initialize Slack Bolt App
app = App(token=SLACK_BOT_TOKEN)

# Define a simple prompt template
template = "You are an assistant. Echo the following message: {text}"
prompt = PromptTemplate(input_variables=["text"], template=template)

# Initialize the OpenAI LLM using the updated package
llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.5)

# Define a Slack slash command handler (e.g., /echo)
@app.command("/echo")
def handle_echo(ack, respond, command):
    # Acknowledge the command
    ack()
    text = command.get("text", "")
    # Format the prompt with the user's text
    prompt_text = prompt.format(text=text)
    # Call the LLM directly with the formatted prompt
    result = llm(prompt_text)
    # Respond back in Slack
    respond(result)

if __name__ == "__main__":
    # Start the Slack app in Socket Mode
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
