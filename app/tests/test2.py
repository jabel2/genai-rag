from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# Equivalent to SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
text = "This is a test document."
query_result = embeddings.embed_query(text)
doc_result = embeddings.embed_documents([text, "This is not a test document."])
print(query_result)
print(doc_result)