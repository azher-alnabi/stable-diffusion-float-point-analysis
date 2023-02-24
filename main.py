from pathlib import Path
from PIL import Image

# Function to generate a pixel map from an image
def generate_pixel_map(image):
    return {(i+1, j+1): image.getpixel((i, j)) for i in range(image.width) for j in range(image.height)}

# List of filenames to be processed
input_directory = Path("input")
filenames = [
    "anything-v4.0-pruned-fp16-vae.png",
    "anything-v4.0-pruned-fp16.png",
    "anything-v4.0-pruned-fp32-vae.png",
    "anything-v4.0-pruned-fp32.png"
]

# Dictionary comprehension to store pixel maps for each image
pixel_maps = {filename: generate_pixel_map(Image.open(input_directory / filename)) for filename in filenames}

# Access the pixel map for a specific image
fp16_vae_pixel_map = pixel_maps["anything-v4.0-pruned-fp16-vae.png"]
fp16_pixel_map = pixel_maps["anything-v4.0-pruned-fp16.png"]
fp32_vae_pixel_map = pixel_maps["anything-v4.0-pruned-fp32-vae.png"]
fp32_pixel_map = pixel_maps["anything-v4.0-pruned-fp32.png"]

# Check if the pixel maps are equal between fp16 and fp32 images for VAE and non-VAE
if fp16_vae_pixel_map == fp32_vae_pixel_map:
    print("Both the (fp16 + VAE) and (fp32 + VAE) images are identical.")
else:
    print("The (fp16 + VAE) and (fp32 + VAE) images are not identical.")

if fp16_pixel_map == fp32_pixel_map:
    print("Both the fp16 and fp32 images are identical.")
else:
    print("The fp16 and fp32 images are not identical.")