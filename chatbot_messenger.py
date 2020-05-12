from flask import Flask, request
import random
from pymessenger.bot import Bot
import main2_chatbot as main2

# App.py fait appel à main 2 qui a le même code que main, mais au lieu de print le retour du chatbot, retourne la réponse du chatbot à app.py
app = Flask(__name__)
ACCESS_TOKEN="EAACGK71vevEBAFF8bIMGLOttaKHarlvS4gZBnw776tfaxYWZCWRiiC30QjTGF4rHvB43DgqD1dqfjOeSuX8YePsNM6BifKRZCj5zgi5YZAXJHv3hMV8NQelAgjZAP7OLnnoEtAUIt09IlGD0XnueFZBDbqY6w2SnjBnLTnxPGwyOWb6ENb5ljb"
VERIFY_TOKEN="RandomPassword"
bot = Bot(ACCESS_TOKEN)

#lE MESSAGE QUE FACEBOOK ENVOIE SERA RECU PAR NOTRE BOT A CET ENDROIT
@app.route("/", methods = ['GET','POST'])


def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else :
        # get whatever message a user send to the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging :
                if message.get('message') :
                    # Facebook Messenger ID for user so we know where to send responses  back
                    recipient_id=message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text=get_message(message['message'].get('text'))
                        send_message(recipient_id, response_sent_text)
                    # If user sends us a GIF, photo, video, or any other nonn-text-items
                    """
                    if message['message'].get('attachments'):
                        response_sent_nontext=get_message()
                        send_message(recipient_id, responses_sent_nontext)
                    """
    return "Message Processed"


def verify_fb_token(token_sent): #VERIFICATION DU TOKEN DE NOTRE BOT ET DE MESSENGER
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def get_message(inp):          #RECUPERE LE MESSAGE ENVOYE PAR LE USER
    return main2.chat(inp)

def send_message(recipient_id, response):
    #RENVOIE UN MESSAGE A L UTILISATEUR
    bot.send_text_message(recipient_id, response)
    return "Success"

if __name__ == "__main__" :
    app.run()
