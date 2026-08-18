from langchain_ollama import OllamaEmbeddings
from modules.chunk_manager import create_chunks
from pathlib import Path
from modules.chroma_manager import update_chroma_collection

EMBEDDINGS_PATH = Path("data/profile_embeddings.json")

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)


def update_profile_embeddings():
    from modules.profile_manager import load_profile

    profile = load_profile()

    if not profile:
        return

    chunks = create_chunks(profile)

    embedded_chunks = generate_embeddings(chunks)

    update_chroma_collection(embedded_chunks)


def generate_embeddings(chunks):
    """
    Generate embeddings for all profile chunks.
    """

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedding_model.embed_documents(texts)

    embedded_chunks = []

    for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

        embedded_chunk = {
            "id": index + 1,
            "section": chunk["section"],
            "project_type": chunk.get("project_type", ""),
            "text": chunk["text"],
            "embedding": embedding,
            "data": chunk.get("data")
        }

        embedded_chunks.append(embedded_chunk)

    return embedded_chunks