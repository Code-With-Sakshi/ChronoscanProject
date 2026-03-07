import cv2

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (512, 512))
    img = cv2.GaussianBlur(img, (5, 5), 0)
    return img
