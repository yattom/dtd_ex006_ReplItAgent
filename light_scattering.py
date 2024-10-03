import numpy as np

def calculate_sky_colors(width, height, sun_angle):
    """
    Calculate sky colors based on simple Rayleigh scattering.
    
    :param width: Image width
    :param height: Image height
    :param sun_angle: Angle of the sun in degrees (0 = horizon, 90 = zenith)
    :return: 3D array of RGB colors
    """
    y = np.linspace(0, 1, height)[:, np.newaxis]
    x = np.linspace(0, 1, width)
    
    # Convert sun angle to radians
    sun_angle_rad = np.radians(sun_angle)
    
    # Calculate sun position
    sun_x = 0.5 + 0.5 * np.cos(sun_angle_rad)
    sun_y = 0.5 * np.sin(sun_angle_rad)
    
    # Calculate distance from each pixel to the sun
    dist_to_sun = np.sqrt((x - sun_x)**2 + (y - sun_y)**2)
    
    # Calculate scattering intensities
    red = np.exp(-dist_to_sun * 3)
    green = np.exp(-dist_to_sun * 5)
    blue = np.exp(-dist_to_sun * 7)
    
    # Combine colors and normalize
    colors = np.stack([red, green, blue], axis=-1)
    colors /= colors.max()
    
    return colors

