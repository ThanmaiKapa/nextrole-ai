from langchain_ollama import OllamaEmbeddings
from modules.profile_manager import load_profile
from modules.chunk_manager import create_chunks
import json
from pathlib import Path
from modules.chroma_manager import update_chroma_collection

EMBEDDINGS_PATH = Path("data/profile_embeddings.json")

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)


def generate_embeddings(chunks):
    """
    Generate embeddings for all profile chunks.

    Returns a list of dictionaries containing:
    - id
    - section
    - text
    - embedding
    """

    # Generate embeddings for all chunks at once
    embeddings = embedding_model.embed_documents(chunks)

    embedded_chunks = []

    for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

        # Determine section name
        section = chunk.split("\n")[0].strip()

        embedded_chunks.append(
            {
                "id": index + 1,
                "section": section,
                "text": chunk,
                "embedding": embedding
            }
        )

    return embedded_chunks

def update_profile_embeddings():

    """
    Load the latest Master Profile, regenerate chunks,
    create embeddings, and update the ChromaDB collection.
    """

    profile = load_profile()

    if not profile:
        return

    chunks = create_chunks(profile)

    embedded_chunks = generate_embeddings(chunks)

    update_chroma_collection(embedded_chunks)