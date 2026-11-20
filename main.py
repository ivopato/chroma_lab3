import chromadb

client = chromadb.HttpClient(host="localhost", port=8000)

collection = client.get_or_create_collection("sentences_collection")

# chat ayudó 1 poco con este for 
sentences = []
ids = []
for line in open("sentences.txt"):
    if line.strip() != "":
        sentences.append(line.strip())
        ids.append("doc" + str(len(sentences)))

collection.add(ids=ids, documents=sentences)

# queries que vamos a usae
query_result = collection.query(
    query_texts=[
        "How do computers understand meaning in language?",
        "How do people start preparing a meal?",
        "What are common ways to move between places?",
        "Which activities require coordination and skill?",
        "What habits support physical well-being?"
    ],
    n_results=3
)

print("QUERIES\n")
for doc_id, doc_text in zip(query_result['ids'], query_result['documents']):
    print(f"Document ID: {doc_id}, Document: {doc_text}\n")


# las nuevas (ai generated ngl)
new_sentences = []
new_ids = []
for line in open("new_sentences.txt"):
    if line.strip() != "":
        new_sentences.append(line.strip())
        new_ids.append("new" + str(len(new_sentences)))

collection.add(ids=new_ids, documents=new_sentences)

query_result = collection.query(
    query_texts=[
        "Why does indoor greenery wither?",
        "Which creatures and natural materials help a backyard flourish?"
    ],
    n_results=3
)

print("QUERIES PROPIAS\n")
for doc_id, doc_text in zip(query_result['ids'], query_result['documents']):
    print(f"Document ID: {doc_id}, Document: {doc_text}\n")

client.delete_collection("sentences_collection")
