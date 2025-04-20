from sentence_transformers import SentenceTransformer
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType

# Connect to Milvus
connections.connect(alias="default", host=os.getenv("MILVUS_HOST", "localhost"), port=os.getenv("MILVUS_PORT", "19530"))

# Load the model
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# Define the schema for Milvus collection
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=500)
]
schema = CollectionSchema(fields, "Document storage for chatbot")
collection = Collection("documents", schema)

def embed_and_store(documents):
    embeddings = model.encode(documents)
    data = [[doc, emb] for doc, emb in zip(documents, embeddings)]
    collection.insert(data)

def search(query):
    query_embedding = model.encode([query])
    results = collection.search(query_embedding, anns_field='embedding', limit=5)
    return [{"text": res.entity.get('text')} for res in results]