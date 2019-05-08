#%%
import os
import fnmatch
import cv2
import glob
import tensorflow as tf
import numpy as np, pandas as pd

import matplotlib.pyplot as plt, seaborn as sns
from keras.preprocessing import image
from keras.models import model_from_yaml

# .swapaxes(a, 2,0)
target_size = 128
img_data_list = []
for filename in glob.glob('DeepFashion/In-shop Clothes Retrieval Benchmark/Img/img_highres/MEN/Jackets_Vests/**/*_front.jpg'):
    img = image.load_img(filename, target_size=(target_size, target_size))

    #To check the image, you can type the following:
    # plt.imshow(img)
    # plt.show()
    # plt.close()

    img_data = image.img_to_array(img)
    # img_data = np.expand_dims(img_data, axis=0)
    img_data_list.append(img_data)

#%%
len(img_data_list[0][0][0])
# temp = pd.read_hdf('DeepFashion/Fashion Synthesis Benchmark/Img/data_release/supervision_signals/G2.h5')
# display(temp.head())
# temp = pd.read_hdf('DeepFashion/Fashion Synthesis Benchmark/Img/data_release/supervision_signals/G2.h5')

#%%
# tf.reset_default_graph()
with tf.Session() as sess:
    saver = tf.train.import_meta_graph('vunet_deepfashion0/model.ckpt-100000.meta')
    saver.restore(sess, "vunet_deepfashion0/model.ckpt-100000")
    print(saver)
    # feed_dict = {tf_train_dataset : batch_data}
    # predictions = sess.run([test_prediction], feed_dict)
    # graph = tf.get_default_graph()
    # input_x = graph.get_tensor_by_name("input_x:0")
    # result = graph.get_tensor_by_name("result:0")

    # feed_dict = {input_x: img_data_list[0]}

    # predictions = result.eval(feed_dict=feed_dict)


#%%
input_x = tf.placeholder(tf.float32, shape=[None, 3], name='input')

with tf.Session() as sess:  
    saver = tf.train.import_meta_graph('vunet_deepfashion0/model.ckpt-100000.meta')
    saver.restore(sess, "vunet_deepfashion0/model.ckpt-100000")
    print(sess.run({}))
# graph = tf.get_default_graph()
# input_x = graph.get_tensor_by_name("input:0")
# op_to_restore = graph.get_tensor_by_name("op_to_restore:0")

# feed_dict = {input_x: img_data_list[0]}
# print(sess.run(op_to_restore, feed_dict))
