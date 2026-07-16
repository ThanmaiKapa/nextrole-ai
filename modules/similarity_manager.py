from modules.chroma_manager import collection
from modules.embedding_manager import embedding_model

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
    dict
        Top matching profile chunks retrieved from ChromaDB.
    """

    # Generate embedding for the query
    query_embedding = embedding_model.embed_query(query)

    results=collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["metadatas", "documents", "distances"]
    )
    return results