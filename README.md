# OpenAI-Automation

Este script faz a integração entre o ChatGPT da OpenAI e uma API de Automação de Dispositivos para enviar comandos para dispositivos.

## Como funciona

O script funciona da seguinte forma:

1. Carrega os comandos que serão fornecidos ao ChatGPT a partir de um arquivo JSON (no exemplo fornecido, o arquivo é automation-db.json).
2. Solicita o comando que será enviado ao ChatGPT para que ele escolha uma opção.
3. Faz a chamada ao ChatGPT com o comando solicitado.
4. Obtém a opção selecionada pelo ChatGPT.
5. Faz a chamada à API de automação correspondente.

O script usa a biblioteca Requests para fazer as chamadas à API e a biblioteca json_reader para carregar o arquivo JSON. O modelo de linguagem usado pelo ChatGPT é o text-davinci-003.

## Como executar

Certifique-se de ter instalado as bibliotecas necessárias (Requests e json_reader).
Defina sua chave de API do OpenAI no seu ambiente local, exportando a variável de ambiente OPENAI_APIKEY.
Crie um arquivo JSON com os comandos para a API de Automação de Dispositivos.
Execute o script usando o comando python nome_do_script.py.

## Exemplo de arquivo JSON

O arquivo JSON deve conter uma lista de objetos, em que cada objeto representa um comando que pode ser enviado para a API de Automação de Dispositivos. Cada objeto deve ter uma opção, que é o texto que o ChatGPT irá apresentar ao usuário, e um request, que é o endpoint da API para enviar o comando. Aqui está um exemplo de como o arquivo JSON pode ser estruturado:

```json
[
  {
    "option": "Ligar a TV",
    "request": "https://api.exemplo.com/tv/on"
  },
  {
    "option": "Desligar a TV",
    "request": "https://api.exemplo.com/tv/off"
  }
]
```

## Observações

O script foi desenvolvido em Python 3 e pode precisar de ajustes se você estiver usando uma versão anterior do Python. Certifique-se de ter instalado as bibliotecas necessárias antes de executar o script.
