import pandas as pd
from loader import load_documents
from agent import process_ticket

def main():
    print("🔄 Loading support documents...")
    documents = load_documents()

    print("📄 Reading support tickets...")
    df = pd.read_csv("../support_tickets/support_tickets.csv")

    results = []

    print("🤖 Processing tickets...")

    for _, row in df.iterrows():
        subject = str(row.get("subject", ""))
        issue = str(row.get("issue", ""))
        text = subject + " " + issue

        result = process_ticket(text, documents)
        results.append(result)

    output_df = pd.DataFrame(results)

    output_path = "../support_tickets/output.csv"
    output_df.to_csv(output_path, index=False)

    print(f"✅ Output saved to {output_path}")


if __name__ == "__main__":
    main()
