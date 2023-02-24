import os
from PIL import Image

def generate_pixel_map(image):
    return {(i+1, j+1): image.getpixel((i, j)) for i in range(image.width) for j in range(image.height)}

# Directory containing input PNG files
input_directory = "input"

# List of filenames
filenames = [
    "anything-v4.0-pruned-fp16-vae.png",
    "anything-v4.0-pruned-fp16.png",
    "anything-v4.0-pruned-fp32-vae.png",
    "anything-v4.0-pruned-fp32.png"
]

# Dictionary comprehension to store pixel maps for each image
pixel_maps = {filename: generate_pixel_map(Image.open(os.path.join(input_directory, filename))) for filename in filenames}

# Access the pixel map for a specific image
fp16_vae_pixel_map = pixel_maps["anything-v4.0-pruned-fp16-vae.png"]
fp16_pixel_map = pixel_maps["anything-v4.0-pruned-fp16.png"]
fp32_vae_pixel_map = pixel_maps["anything-v4.0-pruned-fp32-vae.png"]
fp32_pixel_map = pixel_maps["anything-v4.0-pruned-fp32.png"]

# Check if the pixel maps are equal between fp16 and fp32
print(fp16_vae_pixel_map == fp32_vae_pixel_map)
print(fp16_pixel_map == fp32_pixel_map)

# Check if the pixel maps are equal between none VAE and VAE
print(fp16_pixel_map == fp16_vae_pixel_map)
print(fp32_pixel_map == fp32_vae_pixel_map)