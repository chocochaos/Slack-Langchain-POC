This is a proof of concept for collaborating with multiple AI agents on Slack.

# How to use

## Set up the project

1. `git clone` this repository
2. Run `pip install slack_bolt langchain openai`
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
