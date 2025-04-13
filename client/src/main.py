from datetime import datetime
# ToDO: adicionar uma requisição http para o servidor
# result = analyze_kubernetes_yaml(readFile("../example.yaml"))
# result = result.strip('`').strip().removeprefix('json').strip()
# result = json.loads(result)

# current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M")
# filename = f"output-{current_datetime}.json"
# with open("output.json", "w") as json_file:
#     json.dump(result, json_file, indent=2)


from src.scheduler import start_scheduler

if __name__ == '__main__':
    start_scheduler()