#%%
import os
import glob
import shutil

original_folder = 'step1/output/original/**/**'
fashion_folder = 'step1/output/fashion/**/**'

folder = 'step2/input/' #target
folder_dict = {}

for model_type in ['train', 'test']:
    folder_dict[model_type] = {}
    for num in ['data', '1', '5']:
        d = os.path.join(folder, model_type, num+'/')
        folder_dict[model_type][num] = d
        if not os.path.exists(d):
            os.makedirs(d)
        print(d)

total = 0
for file_path in glob.glob(os.path.join(fashion_folder, '*.jpg')):
    total += 1
print('total image for single round:', total)

i = 1
for file_path in glob.glob(os.path.join(original_folder, '*.jpg')):
    fashion_path = file_path.replace('original', 'fashion')
    j = 1
    k = i - j
    #first round
    shutil.copy2(file_path, os.path.join(folder_dict['train']['data'], str((j-1)*total+i)+'.jpg'))
    shutil.copy2(fashion_path, os.path.join(folder_dict['train']['1'], str((j-1)*total+i)+'.jpg'))
    shutil.copy2(fashion_path, os.path.join(folder_dict['train']['5']
        , str(j*total-(j-1) if i==1
            else (j-1)*total+k)+'.jpg'))
    i += 1

    # if i > 1:
    #     break
