import os, json, base64
import openai



def api_call_text(client, message, model_name = "gpt-4o"):
    

    completion = client.chat.completions.create(
    model=model_name, 
    messages=[{"role": "user", "content": message}]
    )

    return completion.choices[0].message.content

