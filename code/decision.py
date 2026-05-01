def is_high_risk(text):
    text = text.lower()

    risk_keywords = [
        "fraud", "unauthorized", "hacked", "scam",
        "legal", "urgent", "card blocked", "payment failed"
    ]

    return any(k in text for k in risk_keywords)


def decide_status(text, retrieved_doc):
    if is_high_risk(text):
        return "escalated"

    if retrieved_doc is None:
        return "escalated"

    return "replied"
