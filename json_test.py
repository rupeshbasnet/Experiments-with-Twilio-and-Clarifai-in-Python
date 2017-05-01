import json
from clarifai.rest import ClarifaiApp

ap = ClarifaiApp("EzBl0vkR31bYfO0sR4_UjB1QhGZjYZf3pb2ZswAK", "uk9UPJADXmDLh--JKtkUM-HhIVL_OxHpxGqIJ7MP")

model = ap.models.get("general-v1.3")

guess = model.predict_by_url('https://api.twilio.com/2010-04-01/Accounts/AC918f78c7804d5cb61079329e80353001/Messages/MMc6dfc05c0e04e04fa103be456adda013/Media/ME3907af5e6bc065948ef94ef18cc5bd57')

print(guess['outputs'][0]['data']['concepts'][0]['name'])
