from classifier import classify_request, classify_product_area
from retriever import retrieve
from decision import decide_status


def process_ticket(text, documents):
    request_type = classify_request(text)
    product_area = classify_product_area(text)

    retrieved_doc = retrieve(text, documents)
    status = decide_status(text, retrieved_doc)

    if status == "replied" and retrieved_doc:
        response = generate_response(retrieved_doc["text"])
        justification = f"Answer derived from document: {retrieved_doc['source']}"
    else:
        response = "This issue requires escalation to the support team for further assistance."
        justification = "Escalated due to high risk or insufficient matching documentation."

    return {
        "status": status,
        "product_area": product_area,
        "response": response,
        "justification": justification,
        "request_type": request_type
    }


def generate_response(doc_text):
    # simple summarization: first few lines
    lines = doc_text.strip().split("\n")
    clean_lines = [line for line in lines if line.strip() and not line.startswith("#")]

    return " ".join(clean_lines[:3])[:400]
