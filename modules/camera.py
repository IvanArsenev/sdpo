from PIL import Image
import cv2

def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
    """
    Функция для обрезки изображения по центру.
    """
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def make_photo():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite("ava.png", image)
    img = Image.open("./ava.png")
    return crop_center(img, min(img.size), min(img.size))