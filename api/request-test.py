import requests

url = "http://localhost:8000/api/analyze"

payload = {}
files=[
  ('file',('example.yaml',open('C:/Users/vinio/facul/AgentK/docs/example.yaml','rb'),'application/x-yaml'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
