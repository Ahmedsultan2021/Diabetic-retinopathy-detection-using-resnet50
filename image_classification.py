from keras.models import load_model
from keras.utils import load_img
from keras.utils import img_to_array
import numpy as np
import os
# img_path = "95_left.jpeg"
IMAGEDIR = "images/"

HEIGHT = 512
WIDTH = 512
model_path = 'my_dr_model.h5'
model = load_model(model_path)



def classify_image(img_path):
    
    # img_path = os.listdir(IMAGEDIR)[0]
    img_path2 = 'images/'+ img_path

    img = load_img(img_path2, target_size=(HEIGHT, WIDTH))

    img_array = img_to_array(img)

    # Rescale the pixel values to be between 0 and 1
    img_array = img_array / 255.

    # Add a batch dimension to the array
    img_array = np.expand_dims(img_array, axis=0)

    # Make the prediction
    pred = model.predict(img_array)

    # Get the predicted class
    pred_class = np.argmax(pred)

    return {
        "predicted_class" : str(pred_class)
    }
    
    
    
# img_path = os.listdir(IMAGEDIR)[0]
# img_path2 = 'images/'+ img_path

    
# classification_results = classify_image()
# print(classification_results)
