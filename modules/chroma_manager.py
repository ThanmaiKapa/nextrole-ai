from pathlib import Path
import chromadb
from chromadb.config import Settings

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
    """
    Replace the existing Master Profile collection
    with the latest profile embeddings.
    """

    if not embedded_chunks:
        return

    # Remove previous data
    existing = collection.get()

    if existing["ids"]:
        collection.delete(
            ids=existing["ids"]
        )

    # Add latest profile
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
        metadatas=[
            {
                "section": chunk["section"]
            }
            for chunk in embedded_chunks
        ]
    )