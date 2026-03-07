# from ml.segment import segment_tumor
# from ml.measure import tumor_area
# import cv2

# def analyze_change(day0_path, day5_path):
#     mask0 = segment_tumor(day0_path)
#     mask5 = segment_tumor(day5_path)
#     mask5 = cv2.resize(mask5, (mask0.shape[1], mask0.shape[0]))

#     area0 = tumor_area(mask0)
#     area5 = tumor_area(mask5)

#     change = area5 - area0
#     percent = (change / area0) * 100 if area0 > 0 else 0

#     diff = cv2.absdiff(mask5, mask0)
#     cv2.imwrite("results/change_map.png", diff)

#     return area0, area5, percent


# ml/change_detector.py
import cv2
import numpy as np
from ml.segment import segment_tumor

def analyze_change(day0_path, day5_path):
    mask0 = segment_tumor(day0_path)
    mask5 = segment_tumor(day5_path)

    area0 = np.sum(mask0 > 0)
    area5 = np.sum(mask5 > 0)

    percent_change = 0 if area0 == 0 else ((area5 - area0) / area0) * 100

    diff = cv2.absdiff(mask5, mask0)
    cv2.imwrite("results/change_map.png", diff)

    return mask0, mask5, percent_change
