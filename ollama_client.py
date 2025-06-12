import ollama

# initialize client
client = ollama.Client()

# pass model & prompt here
model = "gemma3" #replace model you are using
prompt = "What is lambda in python ?"

# chat method
messages = [{"role": "user", "content": prompt}]
response = client.chat(model=model, messages=messages)
print(f"Non-streaming response from ollama client's chat method: \n {response.message.content}")

response = client.chat(model=model, messages=messages, stream=True)
print(f"Streaming response from ollama client's chat method:\n")
for chunk in response:
  print(chunk['message']['content'], end='', flush=True)


# generate method
prompt = "When & who started facebook ?"
response = client.generate(model=model, prompt=prompt)
print(f"Non-streaming response from ollama client's generate method:\n {response.response}")

response = client.generate(model=model, prompt=prompt, stream=True)
print(f"Streaming response from ollama client's generate method:\n")
for chunk in response:
    print(chunk['response'], end='', flush=True)