#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from noise import snoise2

# Perlin generator
def generate_perlin(width, height, scale, octaves, persistence, lacunarity, seed):
    shape = (height, width)
    world = np.zeros(shape)

    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = snoise2(i / scale, j / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, base=seed)
            
    return world

def pixelate(surface, pixel_size):
    height, width = surface.shape
    pixelated_terrain = np.zeros((height, width))

    for i in range(0, height, pixel_size):
        for j in range(0, width, pixel_size):
            pixel_value = np.mean(surface[i:i+pixel_size, j:j+pixel_size])
            pixelated_terrain[i:i+pixel_size, j:j+pixel_size] = pixel_value

    return pixelated_terrain


