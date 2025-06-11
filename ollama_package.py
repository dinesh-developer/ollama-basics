import ollama

# initialize client
client = ollama.Client()

# pass model & prompt here
model = "gemma3" #replace model you are using
prompt = "What is lambda in python ?"
response = client.generate(model=model, prompt=prompt, stream=True)
# print(f'Response from Ollama: \n {response.response}')
for chunk in response:
    print(chunk['response'], end='', flush=True)



# messages = [{"role": "user", "content": prompt}]
# response = client.chat(model=model, messages=messages, stream=True)
# print(f'Response from Ollama: \n {response.message.content}')

# for chunk in response:
#   print(chunk['message']['content'], end='', flush=True)