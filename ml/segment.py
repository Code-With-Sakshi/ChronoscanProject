# ml/segment.py
import cv2
import numpy as np

def segment_tumor(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(image_path)

    img = cv2.resize(img, (512, 512))
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return mask

