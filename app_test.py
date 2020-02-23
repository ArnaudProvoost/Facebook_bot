import random
from flask import Flask, request
from pymessenger.bot import Bot
app = Flask(__name__)
ACCESS_TOKEN = 'EAAZAoFBaBVKEBALzszJobZCZBAujKeVHk80fxuSz5nXz8ZCNmVX93lL9bmG9U8mnKOr1jspLuNv7agfAGHygJ48aFQzTLpwal7Y0mnYZAXjC8XMEKvNxhI3iaDNXqX2t4baeNcMIITBZAK3Slx57SoktKZCIZAjTdW8RrlwZB0prmsCffmjNWPQ4P'   #ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = 'TOkENfORTeSTING'   #VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot (ACCESS_TOKEN)
welkom = 0

@app.route('/',methods=['GET','POST'])
def receive_message(welkom):

    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if "faq" in message['message'].get('text').lower():
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
                    else:
                        response_sent_nontext = "OK"
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verifaction token'


def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    return random.choice(sample_responses)


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"


def welkom_bericht(welkom):
    if welkom == 0:

        return True
    else:
        return False


if __name__ == '__main__':
    app.run()