import os

def load_documents(data_path="../data"):
    documents = []

    for root, _, files in os.walk(data_path):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        documents.append({
                            "text": content,
                            "source": path
                        })
                except:
                    continue

    return documents
