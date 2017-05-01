from clarifai.rest import ClarifaiApp


def get_guess(image):
    app = ClarifaiApp("EzBl0vkR31bYfO0sR4_UjB1QhGZjYZf3pb2ZswAK", "uk9UPJADXmDLh--JKtkUM-HhIVL_OxHpxGqIJ7MP")
    model = app.models.get("general-v1.3")
    guess = model.predict_by_url([image])
    return guess
