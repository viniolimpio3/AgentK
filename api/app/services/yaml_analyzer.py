import json
from app.utils import util
from app.services import openai
from app.utils.util import getEnv
from app.utils.logger import logger

def analyze(yaml_content, model):
    try:
        client = openai.getClient(model)
        schema = json.loads(util.readFile("./app/utils/schema.json"))
        system_context = """You are a Kubernetes Configuration Agent specialized in identifying misconfigurations, non-compliance, and suboptimal patterns in Kubernetes YAML manifests. Your focus is on validating the files against Kubernetes official best practices, style guidelines, and operational stability—not primarily security issues.
        Analyze the input Kubernetes YAML manifest and output a valid JSON following the specification below.
        - Return a JSON object with a list of issues found, ordered from highest to lowest severity/impact.
        - Each issue must include a concise title, severity level, location details, a detailed description, the relevant Kubernetes standard or best practice violated (if applicable), a reference link, and a recommended fix.
        - Severity levels indicate the impact on deployment or operation:
        - Critical: causes deployment failure, cluster instability, or severe runtime errors.
        - High: can cause unexpected behavior, resource inefficiencies, or important misconfigurations.
        - Medium: non-critical but may lead to degraded performance or maintenance challenges.
        - Low: stylistic or minor best practice improvements that do not affect functionality.
        - Provide an overall score from 0 to 100, starting at 100 and deducting points based on issue severity:
        - -25 for Critical
        - -15 for High
        - -10 for Medium
        - -5 for Low
        - Include a `scoreCriteria` string explaining the scoring breakdown.
        - Provide a `correctedFile` field with the corrected Kubernetes YAML manifest applying the recommended fixes. The YAML should be valid and well-formatted.
        Strictly return only the JSON object that validates against this schema: """ + json.dumps(schema)

        # Other Models:
        response = client.chat.completions.create(
            model=getEnv( 'GPT_AI_MODEL' if model == 'gpt' else 'DPSK_AI_MODEL'),
            messages=[
                {"role": "system", "content": system_context },
                {"role": "user", "content": yaml_content}
            ],
            stream=False
        )

        # o1-mini:
        # response = client.chat.completions.create(
        #     model=getEnv('GPT_AI_MODEL' if model == 'gpt' else 'DPSK_AI_MODEL'),
        #     messages=[
        #         {"role": "user", "content": f"{system_context}\n{yaml_content}"}
        #     ],
        #     stream=False
        # )


        logger.info(f"Response from OpenAI: {response}")
        # Remover o "json" e "```" do final da resposta
        response.choices[0].message.content = json.loads(response.choices[0].message.content.strip('`').strip().removeprefix('json').strip())
        return response
    except Exception as e:
        print(f"Error analyzing YAML content: {e}")
        logger.error(f"Error analyzing YAML content: {e}")
        return {
            "error": str(e),
            "message": "An error occurred while analyzing the YAML content."
        }