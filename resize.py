from PIL import Image

# Load the image
img = Image.open(r"background_118.png")

# Resize the image to the specified resolution of 1280x720
img_resized = img.resize((1280, 720))

# Save the resized image
resized_image_path = r"background_118_resized.png"
img_resized.save(resized_image_path)

resized_image_path
