import cv2
from ml.preprocess import preprocess_image
from ml.change_detection import detect_change
from ml.scoring import calculate_change_score
from ml.genai_report import generate_report

def run_pipeline(image1_path, image2_path):
    img1 = preprocess_image(image1_path)
    img2 = preprocess_image(image2_path)

    diff = detect_change(img1, img2)
    score = calculate_change_score(diff)
    report = generate_report(score)

    heatmap = cv2.applyColorMap(diff, cv2.COLORMAP_JET)
    result_path = "results/diff_heatmap.png"
    cv2.imwrite(result_path, heatmap)

    return {
        "change_score": score,
        "report": report,
        "result_image": result_path
    }
