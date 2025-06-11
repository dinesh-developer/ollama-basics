import requests
import json


## We have 2 ways to hit request, comment-uncomment which one you want to run

url = "http://127.0.0.1:11434/api/chat"

payload = {
    "model": "gemma3",   #model you are using
    "messages": [{"role": "user", "content": "Who was Eda lovelace?"}]
}


response = requests.post(url, json=payload, stream=True) # streaming enabled means not wait for full response

if response.status_code == 200:
    print(f"Streaming response from Ollama: {response} \n")
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                json_data = json.loads(line)
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f'\n Failed to parse line : {line}')

    print() #output streaming complete with a new line

else:
    print(f'Error: {response.status_code}, Message: {response.text}')




# url = "http://127.0.0.1:11434/api/generate"

# payload = {
#     "model": "gemma3",
#     "prompt": "Who was Eda lovelace?"
# }

# response = requests.post(url, json=payload, stream=True)
# if response.status_code == 200:
#     print(f'Ollama Response :\n')
#     for line in response.iter_lines(decode_unicode=True):
#         if line:
#             try:
#                 json_data = json.loads(line)
#                 if "response" in json_data:
#                     print(json_data["response"], end="")
#             except json.JSONDecodeError:
#                 print(f'\n Failed to parse line : {line}')
#     print() #output complete with a new line
# else:
#     print(f'Error: {response.status_code}, Message: {response.text}')