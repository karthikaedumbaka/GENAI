import requests
import time
print("starting................")
def ollama_query(prompt, model="gpt-oss:20b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    start_time = time.time()
    response = requests.post(url, json=payload)
    elapsed_time = time.time() - start_time
    
    print(f"⏱ Took {elapsed_time:.2f} seconds")
    return response.json()['response']

print(ollama_query("Summarize the history of AI in 5 bullet points."))
