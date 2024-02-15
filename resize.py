from PIL import Image
# make sure to install the PIL library
# pip install Pillow


def resize_this_image(path, width, height):
    # Load the image
    img = Image.open(path)

    # Resize the image to the specified resolution of 1280x720
    img_resized = img.resize((width, height)

    # Save the resized image
    resized_image_path = path.replace(".png", "_resized.png")
    img_resized.save(resized_image_path)

# Just update here the path of the image you want to resize
# And the width and height you want to resize it to
resize_this_image(r"background_118.png", 1280, 720)