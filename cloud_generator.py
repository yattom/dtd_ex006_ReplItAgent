import numpy as np
from noise import pnoise2

def generate_clouds(width, height, density):
    """
    Generate cloud patterns using Perlin noise.
    
    :param width: Image width
    :param height: Image height
    :param density: Cloud density (0-1)
    :return: 2D array of cloud alpha values
    """
    scale = 100.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0
    
    cloud_map = np.zeros((height, width))
    
    for y in range(height):
        for x in range(width):
            noise_val = pnoise2(x / scale, 
                                y / scale, 
                                octaves=octaves, 
                                persistence=persistence, 
                                lacunarity=lacunarity, 
                                repeatx=width, 
                                repeaty=height, 
                                base=42)
            cloud_map[y, x] = noise_val
    
    # Normalize and apply density
    cloud_map = (cloud_map - cloud_map.min()) / (cloud_map.max() - cloud_map.min())
    cloud_map = np.clip(cloud_map * density * 2, 0, 1)
    
    return cloud_map

