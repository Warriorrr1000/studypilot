import requests
from config import API_KEY

api_key = API_KEY

url = "https://openrouter.ai/api/v1/chat/completions"

def get_response(prompt: str,instruction: str = "Answer briefly") -> str:
    prompt = prompt.strip()
    if not prompt:
        raise ValueError(f"\'prompt\' is a required argument.")
    try:
        headers = {
    "Authorization": f"Bearer {api_key}"
}
        
        data = {
    "model": "meta-llama/llama-3-8b-instruct",
    "messages": [
        {"role": "user", "content": f"{instruction} : {prompt}"}
    ]
}
        response = requests.post(url, headers=headers, json=data,timeout=30)
        data = response.json()
        return (data["choices"][0]["message"]["content"])
    except Exception as e:
        return f"Error: {e}"
    
