#%%
#copy the selected photos
import os
import glob
import shutil

fashion_folder = 'step1/output/fashion/**/**'
deep_fashion_folder = 'DeepFashion/In-shop Clothes Retrieval Benchmark/Img/img_highres/MEN/'
photo_folder = 'photo'
original_folder = 'step1/output/original'

# for folder in []:
#     if not os.path.exists(folder):
#         os.mkdir(folder)

for file_path in glob.glob(os.path.join(fashion_folder, '*.jpg')):
    file_name = file_path.rsplit('/')[-1]
    fashion_root_folder = fashion_folder.replace('**/**', '')
    root_folder = os.path.dirname(file_path).replace(fashion_root_folder, '')
    photo_dir = os.path.join(photo_folder, root_folder)
    original_dir = os.path.join(original_folder, root_folder)

    deep_fashion = deep_fashion_folder if '_women' not in file_path else deep_fashion_folder.replace('MEN', 'WOMEN')
    if not os.path.exists(photo_dir):
        os.makedirs(photo_dir)
    shutil.copy2(os.path.join(deep_fashion, root_folder.replace('_women', ''), file_name)
        , os.path.join(photo_dir, file_name))

    #generate step1/output/original
    if not os.path.exists(original_dir):
        os.makedirs(original_dir)
    shutil.copy2(os.path.join(deep_fashion, root_folder.replace('_women', ''), file_name)
        , os.path.join(original_dir, file_name))
    # break
