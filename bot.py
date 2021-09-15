#Created by Pedro Martin Gonzalez
#Github user: pedromarting3
#Gmail: pedromarting3@gmail.com
from flask import Flask, request
import requests
import random
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'meme' in incoming_msg:
        # return a meme pic
        meme = ['https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.p50xvro5A0vCuwbis__VEwHaEK%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.qjKx8vrA9ldRyH4dqQEh2gHaFs%26pid%3DApi&f=1',
                'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.3NZ10ojg3oRwh3egy5cL5QHaGT%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.fVvzEruqnJdQW0SLrdFMKgHaEK%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.N3qEig0RrQqLeT51CY4tvgHaNK%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.oUQV_LmmyALzUZw9OYrmwAHaEK%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.IVN790MYqFL7W1BPTPBicAHaJn%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.5Ragro2bwdnarVpH-ihMXwHaEK%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.bxhDGBaBT7CFZL7KmjPongHaEK%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.rg02la01jBqzqQT8sOLkyQHaEK%26pid%3DApi&f=1']

        mostrar = random.choice(meme)
        msg.media(mostrar)
        responded = True
    if 'dog' in incoming_msg:
        # return a dog pic
        perretes = ['https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.GCMcYNnn_pBOGEs656FFDQEkEs%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.rBVQ4LdlQ94lm0w3zgx_zgHaFj%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.vWzdgZ6JrjQfReYUUx-4owHaNJ%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP._4Yvn5Rjgop9eRjkI6CIkwHaHc%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.WWuYU_l8_xQgNk7VVVi5bQHaFX%26pid%3DApi&f=1',
                    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.VY9-YVIblA4ALqxHou3hWwAAAA%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.DvP0bnIfw4mS0nrglNiDnQHaHa%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.KrpQkY0har2H_ztFFJSAKAHaK3%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.Kyslh7GfD2EeNG8r3qDRDQAAAA%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.v2X3SkpUl-sRoQo5bKwvrAHaJn%26pid%3DApi&f=1']
        mostrar = random.choice(perretes)
        msg.media(mostrar)
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()
