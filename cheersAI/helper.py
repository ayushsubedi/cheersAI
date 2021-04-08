from PIL import Image
from torch.autograd import Variable
import torch
import torch.optim as optim
from torchvision import transforms
import time
import os
import copy

def predict_image(image, loaded_model, test_transforms):
    image_tensor = test_transforms(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    _input = Variable(image_tensor)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    _input = _input.to(device)
    output = loaded_model(_input)
    index = output.data.cpu().numpy().argmax()
    return index

def transform_image(image_url):
    test_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    url = "https://zenodo.org/record/4608087/files/model_conv.h5"
    loaded_model = torch.utils.model_zoo.load_url(url, map_location=torch.device('cpu'))
    loaded_model.eval()
    image = Image.open(image_url)
    return str(predict_image(image, loaded_model, test_transforms))