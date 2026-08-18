from pathlib import Path
import chromadb
from chromadb.config import Settings
import json

# -------------------------------------------------------
# ChromaDB Configuration
# -------------------------------------------------------

CHROMA_PATH = Path("data/chroma_db")

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH),
    settings=Settings(anonymized_telemetry=False)
)

# -------------------------------------------------------
# Collection
# -------------------------------------------------------

collection = client.get_or_create_collection(
    name="master_profile"
)


# -------------------------------------------------------
# Save Profile Embeddings
# -------------------------------------------------------

def update_chroma_collection(embedded_chunks):

    if not embedded_chunks:
        return

    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    # ---------------- CREATE METADATA ----------------

    metadatas = [
        {
            "section": chunk["section"],
            "project_type": chunk["project_type"],
            "data": json.dumps(chunk["data"])
            if chunk.get("data") is not None
            else ""
        }
        for chunk in embedded_chunks
    ]

    # ---------------- DEBUG 1 ----------------

    print("\n================ FIRST PROJECT METADATA BEFORE STORE ================\n")

    for metadata in metadatas:
        if metadata["section"] == "Project":
            print(metadata)
            break

    # ---------------- STORE ----------------

    collection.add(
        ids=[
            str(chunk["id"])
            for chunk in embedded_chunks
        ],
        documents=[
            chunk["text"]
            for chunk in embedded_chunks
        ],
        embeddings=[
            chunk["embedding"]
            for chunk in embedded_chunks
        ],
        metadatas=metadatas
    )