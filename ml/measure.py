import cv2
import numpy as np

def tumor_area(mask):
    return np.sum(mask == 255)
