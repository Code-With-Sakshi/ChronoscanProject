import os
import cv2
import csv
from ml.change_detector import analyze_change

YES_DIR = "archive/brain_tumor_dataset/yes"
NO_DIR = "archive/brain_tumor_dataset/no"

os.makedirs("results/changes", exist_ok=True)

csv_file = open("results/chronoscan_results.csv", "w", newline="")
writer = csv.writer(csv_file)
writer.writerow(["image", "tumor_change_percent", "label"])

def process_folder(folder, label):
    images = sorted(os.listdir(folder))

    for i in range(len(images) - 1):
        day0 = os.path.join(folder, images[i])
        day5 = os.path.join(folder, images[i + 1])

        mask0, mask5, diff, percent = analyze_change(day0, day5)

        name = images[i].split(".")[0]
        out_img = f"results/changes/{name}_change.png"

        cv2.imwrite(out_img, diff)

        writer.writerow([name, round(percent, 2), label])

        print(f"✔ {name} | Change: {round(percent,2)}%")

process_folder(YES_DIR, "tumor")
process_folder(NO_DIR, "normal")

csv_file.close()
