from clarifai.rest import ClarifaiApp
import json
from pprint import pprint

with open('../secrets.json') as f:
    secrets = json.load(f)


app = ClarifaiApp(api_key=secrets['CLARIFAI_API_KEY'])

model = app.public_models.general_model
prediction = model.predict_by_filename("/home/pi/pictures/picture2.jpg")
concepts = prediction['outputs'][0]['data']['concepts']
print([x['name'] for x in concepts])
