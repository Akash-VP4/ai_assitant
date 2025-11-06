 
from typing import List, Any
import numpy as np
 

class DB_OPERATIONS:
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
            print(f"[DEGUB]: Added {collection.count()} document to {collection}")

        except Exception as e:
            print(f"[ERORR]: Failed to add documents: {e}")

        
    def retrieve_document(query:np.ndarray, collection, top_k = 3):
        """This will retrieve closest data from db
        Args:
            query:
            collection:
            top_k:
            
        Returns:
        """
    

 

