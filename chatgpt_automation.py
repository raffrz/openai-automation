import os
import requests
import json
import json_reader
from mic_service import MicService

def main():
  # Carrega os comandos que serão fornecidos ao ChatGPT
  commands = load_commands()
  # Solicita o comando que será enviado ao ChatGPT para que ele escolha uma opcão
  mic_service = MicService()
  user_command = mic_service.listen_audio()
  # Faz a chamada ao ChatGPT
  chatgpt_response = execute_chatgpt_request(commands, user_command)
  # Obtem a opcao selecionada pelo ChatGPT
  command = get_selected_command(commands, chatgpt_response)
  # Faz a chamada a API de automacao correspondente
  execute_devices_request(command)

def load_commands():
  options = json_reader.read_json_input_stream(open('automation-db.json'))
  return options

def execute_chatgpt_request(commands, user_command):
  # Defina o endpoint da API
  endpoint = "https://api.openai.com/v1/completions"
  # Defina sua chave de API
  api_key = os.environ["OPENAI_APIKEY"]
  
  # Defina o texto que você quer enviar para a API
  chatgpt_options = ""
  for command in commands:
    chatgpt_options += f" - {command['option']}\n"

  text = f"""Dadas estas opções:\n
  {chatgpt_options}
  Qual destas opções é a adequada quando eu disser '{user_command}'?"""

  # Define os headers da chamada REST
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  # Defina o corpo da chamada REST
  data = {
    "model": "text-davinci-003",
    "prompt": text,
    "temperature": 0,
    "max_tokens": 60,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
  }

  # Realiza a chamada REST à API
  return requests.post(endpoint, headers=headers, json=data)

def get_selected_command(commands, chatgpt_response):
  response_json = chatgpt_response.json()
  chatgpt_decision:str = response_json['choices'].pop()['text']
  for command in commands:
    if (chatgpt_decision.find(command['option']) >= 0):
      print(f'encountrou o comando: {command}')
      return command
  print('não encoutrou nenhum comando')

def execute_devices_request(command) -> requests.Response:
  devices_api_key = "teste-api-key"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {devices_api_key}"
  }
  device_endpoint = command['request']
  data = {
    "command": command['command']
  }
  print(f'comunicando com o dispositivo no endpoint {device_endpoint}')
  response = requests.post(url=device_endpoint, headers=headers, data=json.dumps(data))

  if (response.status_code == 200):
    print('comando enviado ao dispositivo com sucesso')
  else:
    print(f'nao foi possivel se comunicar com o disposivo status_code={response.status_code}')

if (__name__ == '__main__'):
  main()
