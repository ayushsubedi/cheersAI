from PIL import Image
from torch.autograd import Variable
import torch
import torch.optim as optim
from torchvision import transforms
import time
import os
import copy
import string
import random
import cv2
import numpy as np
from functools import wraps
from flask import session
from PIL import Image
import cv2
import imageio

input_size = 229


def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()

def image_is_blurry(path):
  try:
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    # print ("blurry", fm)
    return (fm<10 or fm>200) 
  except:
    return True


def image_is_dark(path):
  try:
    img = imageio.imread(path, as_gray=True)
    val = np.mean(img)
    # print ("dark", val)
    return  (val<8 or val>110)
  except:
    return True


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def findMinDiff(arr): 
    arr = sorted(arr, reverse=True) 
    return arr[0] - arr[1]

def inference_meaning(row_list):
    percent_threshold = 30
    difference_threshold = 5
    row_list = [float(i) for i in row_list]
    if len(row_list)==0:
        return ""
    max_prob = max(row_list)
    difference = findMinDiff(row_list)
    if (max_prob<percent_threshold or difference<difference_threshold):
        return "Consult an opthlmologist. Predicted probability is not high enough or predictions for two grades are similar."
    return ""


def inference_dr(row_list):
    for prediction in row_list:
        prediction['left_inference'] = inference_meaning(prediction.get("prediction_left_all").split())
        prediction['right_inference'] = inference_meaning(prediction.get("prediction_right_all").split())
    return row_list

def inference_glaucoma(row_list):
    return row_list

class ben_color(object):

    def __call__(self, img, sigmaX=10):
        img = np.asarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = self.crop_image_from_gray(img)
        img = cv2.resize(img, (input_size, input_size))
        img = cv2.addWeighted (img, 4, cv2.GaussianBlur(img, (0,0), sigmaX), -4, 128)
        return Image.fromarray(img)

    def crop_image_from_gray(self, img, tol=7):
        if img.ndim ==2:
            mask = img>tol
            return img[np.ix_(mask.any(1),mask.any(0))]
        elif img.ndim==3:
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            mask = gray_img>tol
            
            check_shape = img[:,:,0][np.ix_(mask.any(1),mask.any(0))].shape[0]
            if (check_shape == 0):
                return img 
            else:
                img1=img[:,:,0][np.ix_(mask.any(1),mask.any(0))]
                img2=img[:,:,1][np.ix_(mask.any(1),mask.any(0))]
                img3=img[:,:,2][np.ix_(mask.any(1),mask.any(0))]
                img = np.stack([img1,img2,img3],axis=-1)
            return img

    def __repr__(self):
        return self.__class__.__name__+'()'

def new_filename(patient_id, eye, safe_name):
    return patient_id+'_'+eye+'_'+''.join(random.choice(string.ascii_lowercase) for i in range(10))+'.'+safe_name.split('.')[1]


def predict_image(image, loaded_model, test_transforms):
    image_tensor = test_transforms(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    _input = Variable(image_tensor)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    _input = _input.to(device)
    output = loaded_model(_input)
    x = output.data.cpu().numpy()[0]
    x = [float(i) for i in x]
    norm = [(i-min(x))/(max(x)-min(x)) for i in x]
    norm = [round(100*i/sum(norm), 2) for i in norm]
    pred = x.index(max(x))
    return " ".join(map(str, norm)), pred

def transform_image(image_url):

    test_transforms = transforms.Compose([
        ben_color(),
        transforms.Resize((input_size, input_size)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    loaded_model = torch.load('cheersAI/static/saved_models/24_inceptionnew.h5', map_location=torch.device('cpu'))
    loaded_model.eval()
    image = Image.open(image_url)
    return predict_image(image, loaded_model, test_transforms)

def all_countries():
    return ['Nepal',
        'Afghanistan',
        'Albania',
        'Algeria',
        'Andorra',
        'Angola',
        'Antigua & Deps',
        'Argentina',
        'Armenia',
        'Australia',
        'Austria',
        'Azerbaijan',
        'Bahamas',
        'Bahrain',
        'Bangladesh',
        'Barbados',
        'Belarus',
        'Belgium',
        'Belize',
        'Benin',
        'Bhutan',
        'Bolivia',
        'Bosnia Herzegovina',
        'Botswana',
        'Brazil',
        'Brunei',
        'Bulgaria',
        'Burkina',
        'Burundi',
        'Cambodia',
        'Cameroon',
        'Canada',
        'Cape Verde',
        'Central African Rep',
        'Chad',
        'Chile',
        'China',
        'Colombia',
        'Comoros',
        'Congo',
        'Congo {Democratic Rep}',
        'Costa Rica',
        'Croatia',
        'Cuba',
        'Cyprus',
        'Czech Republic',
        'Denmark',
        'Djibouti',
        'Dominica',
        'Dominican Republic',
        'East Timor',
        'Ecuador',
        'Egypt',
        'El Salvador',
        'Equatorial Guinea',
        'Eritrea',
        'Estonia',
        'Ethiopia',
        'Fiji',
        'Finland',
        'France',
        'Gabon',
        'Gambia',
        'Georgia',
        'Germany',
        'Ghana',
        'Greece',
        'Grenada',
        'Guatemala',
        'Guinea',
        'Guinea-Bissau',
        'Guyana',
        'Haiti',
        'Honduras',
        'Hungary',
        'Iceland',
        'India',
        'Indonesia',
        'Iran',
        'Iraq',
        'Ireland',
        'Israel',
        'Italy',
        'Ivory Coast',
        'Jamaica',
        'Japan',
        'Jordan',
        'Kazakhstan',
        'Kenya',
        'Kiribati',
        'Korea North',
        'Korea South',
        'Kosovo',
        'Kuwait',
        'Kyrgyzstan',
        'Laos',
        'Latvia',
        'Lebanon',
        'Lesotho',
        'Liberia',
        'Libya',
        'Liechtenstein',
        'Lithuania',
        'Luxembourg',
        'Macedonia',
        'Madagascar',
        'Malawi',
        'Malaysia',
        'Maldives',
        'Mali',
        'Malta',
        'Marshall Islands',
        'Mauritania',
        'Mauritius',
        'Mexico',
        'Micronesia',
        'Moldova',
        'Monaco',
        'Mongolia',
        'Montenegro',
        'Morocco',
        'Mozambique',
        'Myanmar',
        'Namibia',
        'Nauru',
        'Netherlands',
        'New Zealand',
        'Nicaragua',
        'Niger',
        'Nigeria',
        'Norway',
        'Oman',
        'Pakistan',
        'Palau',
        'Panama',
        'Papua New Guinea',
        'Paraguay',
        'Peru',
        'Philippines',
        'Poland',
        'Portugal',
        'Qatar',
        'Romania',
        'Russian Federation',
        'Rwanda',
        'St Kitts & Nevis',
        'St Lucia',
        'Saint Vincent & the Grenadines',
        'Samoa',
        'San Marino',
        'Sao Tome & Principe',
        'Saudi Arabia',
        'Senegal',
        'Serbia',
        'Seychelles',
        'Sierra Leone',
        'Singapore',
        'Slovakia',
        'Slovenia',
        'Solomon Islands',
        'Somalia',
        'South Africa',
        'South Sudan',
        'Spain',
        'Sri Lanka',
        'Sudan',
        'Suriname',
        'Swaziland',
        'Sweden',
        'Switzerland',
        'Syria',
        'Taiwan',
        'Tajikistan',
        'Tanzania',
        'Thailand',
        'Togo',
        'Tonga',
        'Trinidad & Tobago',
        'Tunisia',
        'Turkey',
        'Turkmenistan',
        'Tuvalu',
        'Uganda',
        'Ukraine',
        'United Arab Emirates',
        'United Kingdom',
        'United States',
        'Uruguay',
        'Uzbekistan',
        'Vanuatu',
        'Vatican City',
        'Venezuela',
        'Vietnam',
        'Yemen',
        'Zambia',
        'Zimbabwe'
    ]