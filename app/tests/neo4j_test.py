from langchain.docstore.document import Document
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Neo4jVector
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import PyPDFLoader

loader = PyMuPDFLoader("https://www.govinfo.gov/content/pkg/USCODE-2019-title15/pdf/USCODE-2019-title15-chap2B-sec78q.pdf")
docs = loader.load_and_split()
#print(docs[0])
# loader = TextLoader("doc.txt")
# documents = loader.load()
# text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=20)
# docs = text_splitter.split_documents(documents)
print("=> Spit document successfully...")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
print("=> Created embeddings successfully...")

url="bolt://neo4j:7687"
username="neo4j"
password="neo4juser"
print("=> Connected to neo4j successfully...")
# The Neo4jVector Module will connect to Neo4j and create a vector index if needed.

db = Neo4jVector.from_documents(
    docs, HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"), url=url, username=username, password=password, search_type="hybrid",
)
print("=> Created neo4j vectors from documents successfully...")

query = "Who does the Commission shall notify upon request?"
docs_with_score = db.similarity_search_with_score(query, k=5)

for doc, score in docs_with_score:
    print("-" * 80)
    print("Score: ", score)
    print(str(doc.metadata["page"]) + ":", doc.page_content)
    print("-" * 80)

print("=> Complete.")