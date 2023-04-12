####
# Projet test d'utilisation de l'API de ChatGPT en Python pour communiquer avec l'IA d'OpenAI 
# Version : 0.1
# Date : 05/04/2023
# Author : https://www.commentcoder.com/api-chatgpt/
###

import openai

openai.api_key = "sk-XXXXXXX"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Quelle distance sépare la terre de la lune ?"}
    ]
)

print(response)

print(response.choices[0].message.content)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user", "content": "Et pour Jupiter ?"
    }]
)

print(response.choices[0].message.content)

messages = []

messages.append({"role": "system", "content": "Tu es une IA utile qui répond aux questions posées."})

messages.append({"role": "user", "content": "Quelle distance sépare la terre de la lune ?"})

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(completion.choices[0].message.content)

messages.append({"role": "assistant", "content": completion.choices[0].message.content})

messages.append({"role": "user", "content": "Et pour Jupiter ?"})

for message in messages:
    print(message)

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(completion.choices[0].message.content)

