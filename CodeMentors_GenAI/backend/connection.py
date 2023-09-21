import os
from config import open_api_key

def set_env():
    os.environ["OPENAI_API_KEY"] = open_api_key