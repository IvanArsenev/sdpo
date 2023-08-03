from PIL import Image

def get_photo_two(link):
    img = Image.open(link)
    return img