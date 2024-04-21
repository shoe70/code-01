#!/usr/bin/env python3

from perlin_noise import generate_perlin, pixelate
from standard_noise import generate_noise
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from random import randint
import cv2

# Perlin noise
width, height = 550, 800
scale = 50.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = randint(0, 100)
pixel_size = 5

surface = generate_perlin(width, height, scale, octaves, persistence, lacunarity, seed)
pixelated_surface = pixelate(surface, pixel_size)

acolour = mcolors.ListedColormap(['#FF3D3D', '#FFDB47', '#47FF51', '#695087', '#FF81D0'])
bcolour = mcolors.ListedColormap(['#50A9FF', '#73579C', '#5465FF', '#000D85', '#BDC3FF'])
ccolour = mcolors.ListedColormap(['#FF634D', '#1EB100', '#F7BA00', '#FFB200', '#FFFFFF'])
dcolour = mcolors.ListedColormap(['#000000', '#780000', '#FFFFFF', '#FF0000', '#FF7400'])

plt.imshow(pixelated_surface, cmap="terrain", origin='lower')
plt.show()

#  yStandard noise
sample_image = cv2.imread('images/sample_image.png',0)
perlin_noise = cv2.imread('images/sample_image.png',0)
output_image = generate_noise(sample_image, 0.15)
cv2.imwrite('images/output_image.png', output_image)
