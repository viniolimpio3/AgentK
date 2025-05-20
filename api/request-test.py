import requests
import json
from datetime import datetime

url = "http://localhost:8000/api/analyze?model=gpt"

payload = {}
files=[
  ('file',('example.yaml',open('C:/Users/vinio/facul/AgentK/docs/example.yaml','rb'),'application/x-yaml'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

# Salva a resposta em um arquivo JSON
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"response_{current_datetime}.json"

with open(filename, 'w', encoding='utf-8') as f:
    try:
        json.dump(response.json(), f, indent=2, ensure_ascii=False)
    except Exception:
        # Salva o texto bruto se não for JSON
        f.write(response.text)

print(f"Response saved to {filename}")
print(response.text)
# print(response.json())