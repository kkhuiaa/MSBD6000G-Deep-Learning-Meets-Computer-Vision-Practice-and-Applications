#%%
#TODO: Generate the instance segmentation, but not helpful for step2. One can use the segmentation mask to transform the inclined image to the centre.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import shutil

import cv2
import glob
import numpy as np
import os
import sys

op_img_x,op_img_y = 1600,2300

contrast   = 120
brightness = 0
pixel_factor = 127
default_tree = 40
create = cv2.GC_INIT_WITH_RECT

def segment(img_file, output_folder, original_folder, x ,y, w, z, iteration, rgbf, rgbb, img_size_x=300, img_size_y=500):
    imgs = cv2.imread(img_file)
    img = cv2.resize(imgs, (img_size_x,img_size_y))
    
    mask = np.zeros(img.shape[:2],np.uint8)   
    bgdModel = np.zeros((1,65),np.float64)
    
    fgdModel = np.zeros((1,65),np.float64)
    coord = (x,y,w,z)
    
    cv2.grabCut(img,mask,coord,bgdModel,fgdModel,iteration,create)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img_cut = img*mask2[:,:,np.newaxis]
    rese = cv2.resize(img_cut,(op_img_x,op_img_y))
    img_cont = np.int16(rese) 

    img_cont = img_cont*(contrast/1) - contrast + brightness
    img_cont = np.clip(img_cont, 0, 255)
    img_cont = np.where(img_cont > 0, 255, img_cont) #black background to white
    opr = np.uint8(img_cont)
    op1 = opr[np.where((opr == [255,255,255]).all(axis = 2))] = rgbf
    op2 = opr[np.where((opr == [0,0,0]).all(axis = 2))] = rgbb
    
    file_name = img_file.rsplit('/')[-1]
    input_dir = os.path.dirname(img_file)
    created_output_dir = os.path.join(output_folder, input_dir.replace(input_folder.replace('**', ''), ''))
    created_original_dir = os.path.join(original_folder, input_dir.replace(input_folder.replace('**', ''), ''))
    os.makedirs(created_output_dir, exist_ok=True)
    os.makedirs(created_original_dir, exist_ok=True)
    print(os.path.join(created_output_dir, file_name))

    cv2.imwrite(os.path.join(created_output_dir, file_name), opr)
    shutil.copy2(img_file, os.path.join(created_original_dir, file_name))

# p1 = 80-5
# p2 = 10-5
# p3 = 195-5
# p4 = 420+80
# x_po,y_po,w_po,z_po = p1,p2,p3,p4

# input_folder = 'photo/Tees_Tanks/**'
# instance_segmentation_folder = 'step1/output/instance_segmentation/Tees_Tanks'
# original_folder = 'step1/output/original/Tees_Tanks/'

# for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
#     segment(file_path
#         , instance_segmentation_folder
#         , original_folder
#         , x_po, y_po, w_po, z_po
#         , default_tree
#         , [255 ,255, 255], [0, 0, 0]
#     )

# input_folder = 'photo/Sweatshirts_Hoodies/**'
# instance_segmentation_folder = 'step1/output/instance_segmentation/Sweatshirts_Hoodies'
# original_folder = 'step1/output/original/Sweatshirts_Hoodies/'
# for file_path in glob.glob(os.path.join(input_folder, '*_front.jpg')):
#     segment(file_path
#         , instance_segmentation_folder
#         , original_folder
#         , x_po, y_po, w_po, z_po
#         , default_tree
#         , [255 ,255, 255], [0, 0, 0]
#     )
