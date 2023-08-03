from PIL import Image

def get_photo_one(link):
    img = Image.open(link)
    return img