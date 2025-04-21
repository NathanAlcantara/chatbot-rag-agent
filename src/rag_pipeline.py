from sentence_transformers import SentenceTransformer
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType, MilvusClient
import os
from PyPDF2 import PdfReader
from glob import glob
from tqdm import tqdm
import json
from transformers import pipeline

# Load the model
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
# Connect to Milvus
milvus_client = MilvusClient()

collection_name = "documents"

def emb_text(text):
    return model.encode([text])[0]

def embed_and_store():

    text_lines = []

    for file_path in glob("data/*.md", recursive=True):
        with open(file_path, "r") as file:
            file_text = file.read()

        text_lines += file_text.split("# ")

    test_embedding = emb_text("This is a test")
    embedding_dim = len(test_embedding)

    # Check if the collection exists, if not create it
    if milvus_client.has_collection(collection_name):
        milvus_client.drop_collection(collection_name)

    milvus_client.create_collection(
        collection_name=collection_name,
        dimension=embedding_dim,
        metric_type="IP",  # Inner product distance
        consistency_level="Strong",  # Supported values are (`"Strong"`, `"Session"`, `"Bounded"`, `"Eventually"`). See https://milvus.io/docs/consistency.md#Consistency-Level for more details.
    )

    data = []

    for i, line in enumerate(tqdm(text_lines, desc="Creating embeddings")):
        data.append({"id": i, "vector": emb_text(line), "text": line})

    return milvus_client.insert(collection_name=collection_name, data=data)


def search(question):

    search_res = milvus_client.search(
        collection_name=collection_name,
        data=[
            emb_text(question)
        ],  # Use the `emb_text` function to convert the question to an embedding vector
        limit=3,  # Return top 3 results
        search_params={"metric_type": "IP", "params": {}},  # Inner product distance
        output_fields=["text"],  # Return the text field
    )

    retrieved_lines_with_distances = [
        (res["entity"]["text"], res["distance"]) for res in search_res[0]
    ]

    context = "\n".join(
        [line_with_distance[0] for line_with_distance in retrieved_lines_with_distances]
    )

    SYSTEM_PROMPT = f"""
        ### Task:
        Respond to the user query using the provided context, incorporating inline citations in the format [id] **only when the <source> tag includes an explicit id attribute** (e.g., <source id="1">).

        ### Guidelines:
        - If you don't know the answer, clearly state that.
        - If uncertain, ask the user for clarification.
        - Respond in the same language as the user's query.
        - If the context is unreadable or of poor quality, inform the user and provide the best possible answer.
        - If the answer isn't present in the context but you possess the knowledge, explain this to the user and provide the answer using your own understanding.
        - **Only include inline citations using [id] (e.g., [1], [2]) when the <source> tag includes an id attribute.**
        - Do not cite if the <source> tag does not contain an id attribute.
        - Do not use XML tags in your response.
        - Ensure citations are concise and directly related to the information provided.

        ### Example of Citation:
        If the user asks about a specific topic and the information is found in a source with a provided id attribute, the response should include the citation like in the following example:
        * "According to the study, the proposed method increases efficiency by 20% [1]."

        ### Output:
        Provide a clear and direct response to the user's query, including inline citations in the format [id] only when the <source> tag with id attribute is present in the context.

        <context>
        {context}
        </context>

        <user_query>
        {question}
        </user_query>
    """

    # Load a Hugging Face model for text generation
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

    response = qa_pipeline(f"{SYSTEM_PROMPT}")

    return response[0]['generated_text']