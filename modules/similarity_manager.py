import json

from modules.chroma_manager import collection
from modules.embedding_manager import embedding_model


def similarity_search(
    query,
    top_k=3,
    sections=None,
    project_type=None
):
    """
    Find the most relevant profile chunks.

    Args:
        query (str): User query or job description.
        top_k (int): Number of results to return.
        sections (list[str], optional): Restrict to specific sections.
        project_type (str, optional): Restrict to a project type.

    Returns:
        list[dict]
    """

    query_embedding = embedding_model.embed_query(query)

    # -----------------------------------------
    # Build Chroma metadata filter
    # -----------------------------------------

    where_conditions = []

    if sections is not None:
        if len(sections) == 1:
            where_conditions.append({"section": sections[0]})
        else:
            where_conditions.append({"section": {"$in": sections}})

    if project_type is not None:
        where_conditions.append({"project_type": project_type})

    if len(where_conditions) == 0:
        where = None
    elif len(where_conditions) == 1:
        where = where_conditions[0]
    else:
        where = {"$and": where_conditions}

    # -----------------------------------------
    # Query Chroma
    # -----------------------------------------

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where=where,
        include=["documents", "metadatas", "distances"]
    )

    matches = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):

        data = None

        if metadata.get("data"):
            try:
                data = json.loads(metadata["data"])
            except Exception:
                data = None

        matches.append(
            {
                "section": metadata.get("section"),
                "project_type": metadata.get("project_type"),
                "text": document,
                "data": data,
                "distance": distance,
            }
        )

    return matches