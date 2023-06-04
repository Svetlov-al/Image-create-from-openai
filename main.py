import os
import json
import openai
from base64 import b64decode
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = input("Create picture about: ")

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='512x512',
    response_format='b64_json'
)

with open('data.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

image_data = b64decode(response['data'][0]['b64_json'])
file_name = '_'.join(prompt.split(' '))

with open(f'{file_name}.png', 'wb') as file:
    file.write(image_data)
