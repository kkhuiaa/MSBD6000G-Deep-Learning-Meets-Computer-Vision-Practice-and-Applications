#the code has been created with an intention of previewing the entire project
#contributions are welcomed!!!
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import shutil

import cv2
import glob
import numpy as np
import os
import sys
import pandas as pd
# import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Conv2D

from keras.layers import MaxPooling2D
from keras.layers import Dense

from keras.layers import Flatten,Dropout
from keras.models import model_from_json

def predictor(img_file):
    img = cv2.imread(img_file)
    resize = cv2.resize(img,(64,64))
    #resize = np.expand_dims(resize,axis=0)

    img_fin = np.reshape(resize,[1,64,64,3])
    json_file = open('step1/model/binaryfas10.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    

    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("step1/model/binaryfashion.h5")
    # print("Loaded model from disk")
    
    prediction = loaded_model.predict_classes(img_fin)
    
    prediction = np.squeeze(prediction,axis=1)
    predict = np.squeeze(prediction,axis=0)
    return int(predict)

def path_file(file):
    return str(file)

def nn(img_file, output_folder, image_width=300, image_height=500, white_background=True):
    predict = predictor(img_file)
    file = path_file("step1/annotation.csv")
    reader = pd.read_csv(file)
    # print(predict)

    img = cv2.imread(img_file)
    img = cv2.resize(img, (image_width, image_height))
    #seg = image(image,reader.x1[predict],reader.y1[predict],reader.x2[predict],reader.y2[predict],reader.i[predict])
    
    mask = np.zeros(img.shape[:2], np.uint8)
    
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    rect = (reader.x1[predict], reader.y1[predict], reader.x2[predict], reader.y2[predict])
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, reader.i[predict], cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
    
    img_cut = img*mask2[:,:,np.newaxis]
    if white_background:
        img_cut = np.where(img_cut == 0, 255, img_cut) #black background to white
    file_name = img_file.rsplit('/')[-1]
    input_dir = os.path.dirname(img_file)
    # print('input_dir:', input_dir)
    created_dir = os.path.join(output_folder, input_dir.replace(input_folder.replace('**', ''), ''))
    # print(created_dir)
    os.makedirs(created_dir, exist_ok=True)
    print(os.path.join(created_dir, file_name))
    cv2.imwrite(os.path.join(created_dir, file_name), img_cut)

input_folder = 'photo/Tees_Tanks/**'
fashion_folder = 'step1/output/fashion/Tees_Tanks'
for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
    nn(file_path, output_folder=fashion_folder)

input_folder = 'photo/Sweatshirts_Hoodies/**'
fashion_folder = 'step1/output/fashion/Sweatshirts_Hoodies'
for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
    nn(file_path, output_folder=fashion_folder)

input_folder = 'photo/Shirts_Polos/**'
fashion_folder = 'step1/output/fashion/Shirts_Polos'
for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
    nn(file_path, output_folder=fashion_folder)

input_folder = 'photo/Sweaters/**'
fashion_folder = 'step1/output/fashion/Sweaters'
for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
    nn(file_path, output_folder=fashion_folder)

input_folder = 'photo/Jackets_Vests/**'
fashion_folder = 'step1/output/fashion/Jackets_Vests'
for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
    nn(file_path, output_folder=fashion_folder)

input_folder = 'photo/WOMEN/Sweaters_women/**'
fashion_folder = 'step1/output/fashion/Sweaters_women'
for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
    nn(file_path, output_folder=fashion_folder)

input_folder = 'photo/WOMEN/Sweatshirts_Hoodies_women/**'
fashion_folder = 'step1/output/fashion/Sweatshirts_Hoodies_women'
for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
    nn(file_path, output_folder=fashion_folder)

input_folder = 'photo/WOMEN/Tees_Tanks_women/**'
fashion_folder = 'step1/output/fashion/Tees_Tanks_women'
for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
    nn(file_path, output_folder=fashion_folder)
