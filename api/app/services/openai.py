from openai import OpenAI
from app.utils.util import getEnv

def getClient():
    client = OpenAI(api_key=getEnv("API_KEY_OPENAI"), base_url=getEnv("BASE_URL_OPENAI"))
    return client