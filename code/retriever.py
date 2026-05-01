def retrieve(text, documents):
    text = text.lower().split()
    best_doc = None
    max_score = 0

    for doc in documents:
        doc_text = doc["text"].lower()
        score = sum(1 for word in text if word in doc_text)

        if score > max_score:
            max_score = score
            best_doc = doc

    return best_doc
