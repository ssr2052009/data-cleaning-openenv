def normalize(text):
    return text.lower().replace(" ", "").replace(",", "")


def grade(pred, actual):
    if pred.strip() == "":
        return 0.0

    pred_n = normalize(pred)
    actual_n = normalize(actual)

    if pred_n == actual_n:
        return 1.0

    score = 0.0
    if "name" in pred_n:
        score += 0.3
    if "age" in pred_n:
        score += 0.3
    if "city" in pred_n:
        score += 0.4

    return round(score, 2)