import openai 
import gradio as gr #Pour créer l'inteface web

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Attribuer un rôle à l'IA
messages = [
    {"role": "system", "content": "You are an AI specialized in Food. Do not answer anything other than food-related queries."},
]

# La fonction "chatbot" est définie, qui prend une entrée de l'utilisateur et renvoie une réponse du chatbot.
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
    chat = openai.Completion.create(
        engine="text-davinci-002",
        prompt="".join(message["content"] for message in messages),
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    reply = chat.choices[0].text
    messages.append({"role": "assistant", "content": reply})
    return reply

inputs = gr.inputs.Textbox(lines=7, label="Bonjour commandant, posez vos questions ici!")
outputs = gr.outputs.Textbox(label="Réponse")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="2001, l'Odyssée de l'espace", description="HAL 9000", layout="compact", theme="compact").launch(share=True)
