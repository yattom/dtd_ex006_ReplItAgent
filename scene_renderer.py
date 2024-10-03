import numpy as np

def render_scene(sky_colors, clouds):
    """
    Render the final scene by combining sky colors and clouds.
    
    :param sky_colors: 3D array of RGB sky colors
    :param clouds: 2D array of cloud alpha values
    :return: 3D array of the final rendered image
    """
    # Create cloud color (white)
    cloud_color = np.ones_like(sky_colors) * 0.9
    
    # Blend clouds with sky
    cloud_mask = clouds[:, :, np.newaxis]
    blended_scene = sky_colors * (1 - cloud_mask) + cloud_color * cloud_mask
    
    # Ensure values are in the valid range [0, 1]
    blended_scene = np.clip(blended_scene, 0, 1)
    
    return blended_scene

