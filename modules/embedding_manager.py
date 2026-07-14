from langchain_ollama import OllamaEmbeddings
from modules.profile_manager import load_profile
from modules.chunk_manager import create_chunks
import json
from pathlib import Path

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

def save_embeddings(embedded_chunks):
    """
    Save the embedded chunks to a JSON file.
    """
    
    if not embedded_chunks:
        return
    
    EMBEDDINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(EMBEDDINGS_PATH, "w", encoding="utf-8") as file:
        json.dump(embedded_chunks, file, indent=4)

def update_profile_embeddings():

    """
    Load the latest Master Profile, regenerate chunks,
    create embeddings, and save them locally.
    """

    profile = load_profile()

    if not profile:
        return

    chunks = create_chunks(profile)

    embedded_chunks = generate_embeddings(chunks)

    save_embeddings(embedded_chunks)