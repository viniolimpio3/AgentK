from openai import OpenAI
from app.utils.util import getEnv

def getClient(llm = 'gpt'):
    client = OpenAI(
        api_key=getEnv('GPT_API_KEY_OPENAI' if llm == 'gpt' else 'DPSK_API_KEY_OPENAI'),
        base_url=getEnv('GPT_BASE_URL_OPENAI' if llm == 'gpt' else 'DPSK_BASE_URL_OPENAI'),
        organization=getEnv("OPENAI_ORG_ID")
    )
    return client