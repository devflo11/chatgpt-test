import openai 
import gradio as gr

#Entrez le token de votre API OpenAI
openai.api_key = "Your API Key"
#Message de bienvenue
messages = [{"role": "system", "content": "Bonjour, je suis votre conseiller en développement web. Comment puis-je vous aider aujourd'hui?"}]

#La fonction "chatbot" est définie, qui prend une entrée de l'utilisateur et renvoie une réponse du chatbot.
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
    chat = openai.Completion.create(
        engine="text-davinci-002",
        prompt="".join(message["content"] for message in messages),
       #Configuration du niveau de compétence
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    reply = chat.choices[0].text
    messages.append({"role": "assistant", "content": reply})
    return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat avec un conseiller en développement web")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Conseiller en développement web", description="Posez toutes vos questions sur le développement web", layout="compact", theme="compact").launch(share=True)
