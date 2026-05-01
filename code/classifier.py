def classify_request(text):
    text = text.lower()

    if any(k in text for k in ["feature", "add", "request", "improve"]):
        return "feature_request"
    elif any(k in text for k in ["error", "bug", "not working", "fail", "crash"]):
        return "bug"
    elif any(k in text for k in ["issue", "problem", "help", "unable", "can't"]):
        return "product_issue"
    else:
        return "invalid"


def classify_product_area(text):
    text = text.lower()

    if any(k in text for k in ["payment", "refund", "billing", "charge", "card"]):
        return "billing"
    elif any(k in text for k in ["login", "password", "account", "signin"]):
        return "account"
    elif any(k in text for k in ["test", "assessment", "screen", "candidate"]):
        return "screen"
    elif any(k in text for k in ["api", "integration"]):
        return "developer"
    else:
        return "general"
