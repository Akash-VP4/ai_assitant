from typing import List, Any
import numpy as np


def add_document(document: list[Any], embeddings: np.array,collection):
    """This will add document to vector db
    Args:
        document:
        embeddings:
        collection:
    """

    if len(document['ids']) != len(embeddings):
        raise ValueError(
            f"Number of document({len(document['ids'])}) must match number of embedding({len(embeddings)})"
        )

    try:
        # print(document["documents"])
        collection.add(
            ids=document["ids"],
            documents=document["documents"],
            embeddings=embeddings,
            metadatas=document["metadatas"],
        )
        # print(f"[DEGUB]: Added {collection.count()} document to {collection}")

    except Exception as e:
        print(f"[ERORR]: Failed to add documents: {e}")


def retrieve_document(query_embedding:np.ndarray, collection, n_results = 3,metadata = None, score_threshold:float= -0.01):
    """This will retrieve closest data from db
    Args:
        query:
        collection:
        n_results:
        
    Returns:
    """

    try:
        
        results = collection.query(
            query_embeddings = [query_embedding.tolist()],
            n_results = n_results,
            # where = metadata
        )

        # print("After querying..",results)
        documents = results["documents"][0]
        distances = results["distances"][0]
        metadatas = results["metadatas"][0]
        ids = results["ids"][0]

        retrieved_docs =[]
        retrived_metadtas=[]
        retrieved_ids =[]

        for i,(doc, dist, metadata,id) in enumerate(zip(documents,distances,metadatas,ids)):
            similarity_score = 1-dist

            # print(similarity_score)
            if similarity_score>score_threshold:
                retrieved_docs.append(doc)
                retrived_metadtas.append(metadata["url"])
                retrieved_ids.append(id)
                # print(f"[DEBUG]: Found matching context: {i}")

        # print("[DEBUG]: retrieving completed")

        results = {
            "documents": documents,
            "metadatas": metadatas,
            "ids": ids,
        }

        return results if len(retrieved_docs) > 0 else None

    except Exception as e:
        print(f"[ERROR]: Failed to search: {e}")

    return []
