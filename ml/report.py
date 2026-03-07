# def generate_report(percent):
#     if percent > 15:
#         return "Significant tumor progression observed. Immediate clinical review recommended."
#     elif percent > 5:
#         return "Moderate tumor growth detected. Follow-up advised."
#     elif percent < -5:
#         return "Tumor regression observed. Treatment appears effective."
#     else:
#         return "No significant change in tumor size detected."
# ml/report.py
def generate_report(percent):
    if percent > 15:
        return "Significant tumor progression detected."
    elif percent > 5:
        return "Moderate tumor growth detected."
    elif percent < -5:
        return "Tumor regression detected."
    else:
        return "No significant change detected."
