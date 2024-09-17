embedding_model = SentenceTransformer('BAAI/bge-base-en-v1.5', cache_folder=".")
from langchain.embeddings import HuggingFaceEmbeddings