import numpy as np
import random
import cv2
import scipy.ndimage
from matplotlib  import pyplot as plt


def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('Imagen1.jpg')
noise_img = sp_noise(image,0.05)

result = scipy.ndimage.maximum_filter(noise_img, size=3)  #filtro maximo

plt.subplot(131),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(noise_img),plt.title('Ruido Pimienta')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(result),plt.title('Filtrado')
plt.xticks([]), plt.yticks([])
plt.show()
