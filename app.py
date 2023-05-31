# import torch
# import pickle
# from PIL import Image
# from fastai.vision.all import *
# from fastai.losses import FlattenedLoss
# from fastai.imports import *
# from fastai.torch_imports import *
# from fastai.torch_core import *
# from fastai.layers import *

# def preprocess_image(image_path):
#     image = Image.open(image_path)
#     image = image.resize((224, 224))
#     image = np.array(image)
#     image = np.transpose(image, (2, 0, 1))
#     image = image.astype('float32') / 255
#     image = torch.from_numpy(image)
#     image = image.unsqueeze(0)
#     return image

# def run_model(image_path, model_path):
#     # Load the learner with the `pickle_module` argument set to `pickle`
#     learn = load_learner(model_path, pickle_module=pickle)
#     learn.loss_func = FlattenedLoss()
#     learn.eval()
#     image = preprocess_image(image_path)
#     with torch.no_grad():
#         output, _ = learn.predict(Image.fromarray(np.transpose(image[0].numpy(), (1, 2, 0))))
#         predicted = output.argmax().item()
#     return predicted

# result = run_model("16_right.jpeg", "export.pkl")
# print(result)