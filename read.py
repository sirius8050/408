# !/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import os
import json
from imutils import paths
from keras.preprocessing.image import img_to_array
with open("/home/zhuxianzhi/plant/trainingset/AgriculturalDisease_train_annotations.json", 'r') as f:
  data = json.loads(f.read())
# data = json.loads("D:/BaiduNetdiskDownload/2018 AI CHALLENGER 农作物病害识别/trainingset/AgriculturalDisease_train_annotations.json", 'r')
# print(data[1])
train_data = []
train_labels = []
train_name = []
path = r'/home/zhuxianzhi/plant/trainingset/images/'

a = 0
label=0
imagepath = sorted(list(paths.list_images(path)))
for i in imagepath:
    a = a + 1
    if(a % 100 == 0):
        print(a, '/', len(data))
    image = cv2.imdecode(np.fromfile(i, dtype=np.uint8), cv2.IMREAD_COLOR)
    c = os.path.splitext(i)[0][len(path):len(path)+19]
    print(c)
    for j in range(len(data)):
        b = data[j]['image_id'][0:19]
        if b==c:
            label = int(data[j]['disease_class'])
            break
    # print(image)

    image = cv2.resize(image, (224, 224))
    # train_name.append(i)
    image = img_to_array(image)
    train_data.append(image)
    train_labels.append(label)


train_data = np.array(train_data)
train_labels = np.array(train_labels)

np.save('train_data.npy', train_data)
np.save('train_labels.npy', train_labels)
