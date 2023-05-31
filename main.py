#upload/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from image_classification import classify_image

# import os
# from random import randint
import uuid
# from keras.models import load_model
# from keras.utils import load_img
# from keras.utils import img_to_array
# import numpy as np

 
IMAGEDIR = "images/"
 
app = FastAPI()
 
 
@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
 
    file.filename = f"{uuid.uuid4()}.jpg"
    # file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    # save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    
    classification_results = classify_image(file.filename)
    # attach uploaded filename in result
    #classification_results["uploaded_filename"] = file.filename 
    return classification_results

 
# classification_results = classify_image()  
# print(classification_results)
    
 
 
 
# @app.get("/show/")
# async def read_random_file():
 
#     # get random file from the image directory
#     files = os.listdir(IMAGEDIR)
#     random_index = randint(0, len(files) - 1)
 
#     path = f"{IMAGEDIR}{files[random_index]}"
     
#     return FileResponse(path)