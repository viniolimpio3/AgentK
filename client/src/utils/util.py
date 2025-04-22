import os 

from dotenv import load_dotenv
load_dotenv()

def getEnv(key):
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} not set.")
    return value