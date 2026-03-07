import numpy as np

def calculate_change_score(diff):
    score = np.mean(diff)
    return round(score, 2)
