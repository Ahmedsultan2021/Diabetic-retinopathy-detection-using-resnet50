import json
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    from flask import Flask, jsonify
    from flask_cors import CORS
    from keras.models import load_model
    from keras.utils import load_img
    from keras.utils import img_to_array
    import numpy as np

    HEIGHT = 512
    WIDTH = 512
    model_path = 'my_dr_model.h5'
    model = load_model(model_path)
    img_path = "111_left.jpeg"
    img = load_img(img_path, target_size=(HEIGHT, WIDTH))

    img_array = img_to_array(img)

    # Rescale the pixel values to be between 0 and 1
    img_array = img_array / 255.

    # Add a batch dimension to the array
    img_array = np.expand_dims(img_array, axis=0)

    # Make the prediction
    pred = model.predict(img_array)

    # Get the predicted class
    pred_class = np.argmax(pred)

    print(" the class is ",pred_class)
    return json.dumps({'name': pred_class,
                       'email': 'alice@outlook.com'})
app.run()