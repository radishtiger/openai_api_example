import json
import openai

from utils import api_call_text


with open('keys.json') as f:
    keys = json.load(f)
    
private_key = keys['OPENAI_API_KEY']
organization_key = keys['OPENAI_API_ORGANIZATION_ID']


client = openai.OpenAI(
    api_key = private_key,
    organization = organization_key
)

print("api_call_text")
print(api_call_text(client, "저녁 메뉴 추천해줘"))
print("======\n\n")
