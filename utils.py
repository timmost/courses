import os
from anthropic import Anthropic

def get_client():
    return Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))