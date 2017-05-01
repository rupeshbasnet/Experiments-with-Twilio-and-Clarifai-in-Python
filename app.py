from flask import Flask, request
from twilio import twiml
import json
import urllib.parse
from clarifai.rest import ClarifaiApp


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    print('inside the main function')
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    # resp.message('Hello {}, I know Bibek {}'.format(number, message_body))
    ap = ClarifaiApp("EzBl0vkR31bYfO0sR4_UjB1QhGZjYZf3pb2ZswAK", "uk9UPJADXmDLh--JKtkUM-HhIVL_OxHpxGqIJ7MP")
    model = ap.models.get("general-v1.3")
    image_url = request.form['MediaUrl0']

    guess = model.predict_by_url(image_url)

    # guess = guess['outputs'][0]['data']['concepts'][0]['name']

    print(image_url)

    output = guess['outputs'][0]['data']['concepts'][0]['name']
    resp.message('Your image was ' + str(output))
    # resp.message('got the message')
    print(output)
    return str(resp)

if __name__ == '__main__':
    app.run()


