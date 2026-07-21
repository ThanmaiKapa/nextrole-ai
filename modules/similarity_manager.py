from modules.chroma_manager import collection
from modules.embedding_manager import embedding_model

def similarity_search(query, top_k=3):
    """
    Find the most relevant profile chunks for the given query.
    """

    query_embedding = embedding_model.embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["metadatas", "documents", "distances"]
    )

    matches = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for document, metadata, distance in zip(documents, metadatas, distances):
        matches.append({
            "section": metadata["section"],
            "text": document,
            "distance": distance
        })

    return matches