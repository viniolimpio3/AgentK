import json
from app.utils import util
from app.services import openai
from app.utils.util import getEnv


def analyze(yaml_content, model):
    client = openai.getClient(model)

    schema = json.loads(util.readFile("./app/utils/schema.json"))
    system_context = "You are an Agent that helps identify misconfigurations and issues in Kubernetes YAML files. You will return a valid JSON with a list of issues found, ordered by severity. You will return a JSON with this spec: " + json.dumps(schema)

    response = client.chat.completions.create(
        model=getEnv( 'GPT_AI_MODEL' if model == 'gpt' else 'DPSK_AI_MODEL'),
        messages=[
            {"role": "system", "content": system_context },
            {"role": "user", "content": yaml_content}
        ],
        stream=False
    )
    # Remover o "json" e "```" do final da resposta
    response.choices[0].message.content = json.loads(response.choices[0].message.content.strip('`').strip().removeprefix('json').strip())
    return response