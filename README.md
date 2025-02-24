This is a proof of concept for collaborating with multiple AI agents on Slack.

# How to use

## Set up the project

1. `git clone` this repository
2. Run `pip install -r requirements.txt`
3. Run `source venv/bin/activate`
4. Copy the `.env.example` file to `.env`. Follow the stepts below to get the necessary tokens.

## Create a Slack App

1. Go to [Slack API](https://api.slack.com/apps) and create a new app.
2. Name your app and select a workspace.
3. Under `Socket Mode`
   - Enable Socket Mode
   - Generate an app token. The app token starts with `xapp-`.
   - Copy the app token and use it in your `.env` file.
4. Under `Event Subscriptions`
   - Enable events
   - Subscribe to bot events:
     - `message.channels`
     - `message.groups`
     - `message.im`
     - `message.mpim`
5. Under `OAuth & Permissions`
   - Add the following scopes:
      - `app_mentions:read`
      - `chat:write`
   - Install the app to your workspace.
   - Copy the `Bot User OAuth Token` (starting with `xoxb-`) and use it in your `.env` file.

## Get your OpenAI token

1. Go to [OpenAI](https://platform.openai.com/) and create an account (or log in).
2. Under `Billing`, add a payment method and add some funds to your account.
3. Under `API Keys`, create a new API key.
4. Copy the API key and use it in your `.env` file.

## Run the project

1. Make sure all environment variables are set in `.env`.
2. Run `python main.py`.
3. Invite the bot to a channel using `/invite @your-bot-name`.
4. Interact with an agent by mentioning it in a message, prefixed with an `!`. For example, `Hello !echo, what's up?`.

## Agent Configuration

Each agent's behavior can be customized through a YAML configuration file located in its directory. For example, the Echo agent's configuration is in `src/agents/echo/config.yaml`.

### Configuration Parameters

- `agent_name`: The name used to invoke the agent in Slack (e.g., "echo" for `!echo`)
- `prompt_template`: The template used to format the agent's instructions to the LLM
- `temperature`: Controls the randomness of the LLM's responses (0.0 for deterministic, higher values for more creative responses)

### Example Configuration

```yaml
# src/agents/echo/config.yaml
agent_name: "echo"
prompt_template: "Echo the following message: {text}"
temperature: 0.5
```

To modify an agent's behavior:
1. Locate its configuration file in `src/agents/config/`
2. Adjust the parameters as needed
3. Restart the application for changes to take effect
