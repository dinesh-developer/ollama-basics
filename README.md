# ollama-basics

Here we are learning some basic endpoints that ollama provides us. We'll hit them & see the generated response.

Below are few commands, you can play with them after installing ollama locally.

. Pull a model : ollama pull {model_name}
. Remove a model : ollama rm {model_name}
. Create a model : ollama create {desired_model_name} -f Modelfile
. Copy a model : ollama cp {model_name} {new_model_name}
. Show model information : ollama show {model_name}
. List models on your computer : ollama list
. List which models are currently loaded : ollama ps
. Stop a model which is currently running : ollama stop {model_name}
. Start Ollama : ollama serve  (used when you want to start ollama without running the desktop application.)


To see available model & installation checkout below links:
1. https://github.com/ollama/ollama?tab=readme-ov-file#model-library
2. https://ollama.com/search


Little context what we are covering here : 

We'll be exploring particularly 2 endpoints available '/api/generate' (for single-turn completions) and '/api/chat' (for conversational turns).


We have concept of "Streaming vs. Non-Streaming" responses.
    - refers to how the API response is sent over HTTP to your client. It's controlled by the stream parameter in your request payload.
    - By default, the '/api/chat' endpoint is streaming in nature, while the '/api/generate' endpoint is not. For both endpoints, you can explicitly control streaming behavior using the stream parameter in your request payload.


We have concept of "Structured Output"
    - This is a different concept and refers to constraining the content of the LLM's response to adhere to a specific JSON schema. This is controlled by the format parameter in your request payload (typically set to "json" or a JSON schema definition)


Also how to create/update model. (by using Modelfile) 
    - use above create command then run it.
    - give prompt like 'Who are you' & it's response should be about superman if you use the given Modelfile as it is.