from ml.change_detector import analyze_change
from ml.report import generate_report
import cv2

day0 = "archive/brain_tumor_dataset/yes/Y10.jpg"
day5 = "archive/brain_tumor_dataset/yes/Y15.jpg"


a0, a5, percent = analyze_change(day0, day5)
report = generate_report(percent)

print("Day-0 Area:", a0)
print("Day-5 Area:", a5)
print("Change %:", round(percent, 2))
print("Report:", report)

img = cv2.imread("results/change_map.png", 0)
cv2.imshow("Tumor Change Map", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

