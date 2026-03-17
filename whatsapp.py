from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils.chat import responder

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get("Body")

    resposta, _ = responder(msg)

    resp = MessagingResponse()
    resp.message(resposta)

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
