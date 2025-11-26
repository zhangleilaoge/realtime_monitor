import os
from dotenv import load_dotenv
load_dotenv()

API_KEY   = os.getenv("OPENAI_API_KEY")
BASE_URL  = os.getenv("OPENAI_BASE_URL")
MODEL     = "gpt-3.5-turbo"
SYSTEM_PROMPT = "You are a helpful assistant."
HISTORY_FILE  = "chat_history.json"