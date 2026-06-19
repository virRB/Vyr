import requests

def askAI(prompt=None, personality=None):
    if not prompt:
        return "Error"
    if personality:
        prompt = prompt + f"; make your answer {personality}"
    try:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3:latest",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        return r.json()["response"]
    except Exception as e:
        print(f'Lol there was some error idk read it: {e}')
        return "Error"