import numpy as np
import matplotlib.pyplot as plt
from light_scattering import calculate_sky_colors
from cloud_generator import generate_clouds
from scene_renderer import render_scene

def main():
    print("Sunset Image Generator")
    
    # Get user input
    sun_angle = float(input("Enter sun angle (0-90 degrees): "))
    cloud_density = float(input("Enter cloud density (0-1): "))
    
    # Set image dimensions
    width, height = 800, 600
    
    # Generate sky colors
    sky_colors = calculate_sky_colors(width, height, sun_angle)
    
    # Generate clouds
    clouds = generate_clouds(width, height, cloud_density)
    
    # Render the scene
    image = render_scene(sky_colors, clouds)
    
    # Display the image
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    
    # Save the image
    plt.imsave('sunset_scene.png', image)
    print("Image saved as 'sunset_scene.png'")

if __name__ == "__main__":
    main()
