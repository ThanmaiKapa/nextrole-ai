import json
from pathlib import Path

from sklearn.metrics.pairwise import cosine_similarity
from langchain_ollama import OllamaEmbeddings

EMBEDDINGS_PATH = Path("data/profile_embeddings.json")

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)


def similarity_search(query, top_k=3):
    """
    Find the most relevant profile chunks for the given query.

    Parameters
    ----------
    query : str
        User query or Job Description.

    top_k : int
        Number of most relevant chunks to return.

    Returns
    -------
    list
        Top matching chunks sorted by cosine similarity.
    """

    if not EMBEDDINGS_PATH.exists():
        return []

    with open(EMBEDDINGS_PATH, "r", encoding="utf-8") as file:
        embedded_chunks = json.load(file)

    if not embedded_chunks:
        return []

    # Generate embedding for the query
    query_embedding = embedding_model.embed_query(query)

    results = []

    for chunk in embedded_chunks:

        score = cosine_similarity(
            [query_embedding],
            [chunk["embedding"]]
        )[0][0]

        results.append(
            {
                "id": chunk["id"],
                "section": chunk["section"],
                "text": chunk["text"],
                "similarity_score": float(score)
            }
        )

    results.sort(
        key=lambda x: x["similarity_score"],
        reverse=True
    )

    return results[:top_k]