#!/usr/bin/env python
# coding: utf-8



import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd

bottom_left = cv2.imread('Dataset/bottom_left.jpg')
rgb_bottom_left = cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB)

bottom_right = cv2.imread('Dataset/bottom_right.jpg')
rgb_bottom_right = cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB)

center = cv2.imread('Dataset/center.jpeg')
rgb_center = cv2.cvtColor(center, cv2.COLOR_BGR2RGB)

top_left = cv2.imread('Dataset/top_left.jpg')
rgb_top_left = cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB)

top_right = cv2.imread('Dataset/top_right.jpg')
rgb_top_right = cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB)



# for rgb_bottom_left
print(rgb_bottom_left.shape)
plt.imshow(rgb_bottom_left)

# for rgb_bottom_right
print(rgb_bottom_right.shape)
plt.imshow(rgb_bottom_right)

# for rgb_center
print(rgb_center.shape)
plt.imshow(rgb_center)

# for rgb_top_left
print(rgb_top_left.shape)
plt.imshow(rgb_top_left)

# for rgb_top_right
print(rgb_top_right.shape)
plt.imshow(rgb_top_right)

plt.axis("off")

crop_rgb_bottom_left = cv2.resize(rgb_bottom_left, (200,200))
plt.imshow(crop_rgb_bottom_left)

crop_rgb_bottom_right = cv2.resize(rgb_bottom_right, (200,200))
plt.imshow(crop_rgb_bottom_right)

crop_rgb_center = cv2.resize(rgb_center, (100,100))
plt.imshow(crop_rgb_center)

crop_rgb_top_left = cv2.resize(rgb_top_left, (200,200))
plt.imshow(crop_rgb_top_left)

crop_rgb_top_right = cv2.resize(rgb_top_right, (200,200))
plt.imshow(crop_rgb_top_right)

blank_image = np.zeros(shape=[430,430,3], dtype=np.uint8)

blank_image[10:210, 10:210,:] = crop_rgb_top_left

blank_image[220:420, 10:210,:] = crop_rgb_bottom_left

blank_image[10:210, 220:420,:] = crop_rgb_top_right

blank_image[220:420, 220:420,:] = crop_rgb_bottom_right

blank_image_center = np.zeros(shape=[120,120,3], dtype=np.uint8)
blank_image_center[10:110, 10:110,:] = crop_rgb_center

blank_image[155:275, 155:275,:] = blank_image_center

plt.imshow(blank_image)
plt.axis("off")
plt.show()


# shape of image
#blank_image.shape

# convert image to array
array = np.array(blank_image)

array = array.reshape(430*430,3)

# np.savetxt('abc.csv',array,fmt="%d",header="r,g,b")


pokemons = {
    "r":array[:,0],
    "g":array[:,1],
    "b":array[:,2]
    }

df = pd.DataFrame(pokemons)

df.to_csv('pokemon_data.csv', index=False)
