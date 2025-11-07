import os
import chromadb
from typing import List, Any
import numpy as np
from src.embedd import Embedding
from src.db_ops import add_document,retrieve_document


class ChromaVectorStore:

    def __init__(
        self,
        embedding: Embedding = Embedding(),
        collection_main_name="web_data",
        persistent_directory="./db",
        collection_page_name="page_data",
    ):

        self.embedd = embedding
        self.persistent_directory = persistent_directory
        self.client = None
        self.collection_main = self._initialize_store(collection_main_name)
        self.collection_page = self._initialize_store(collection_page_name)

    def _initialize_store(self, collection_name):
        """This will initialize store
        Args:
            collection_name:

        Returns:
            ineatialized collection"""

        try:
            os.makedirs(self.persistent_directory, exist_ok=True)
            self.client = chromadb.PersistentClient(path=self.persistent_directory)
            collection = self.client.get_or_create_collection(
                name=collection_name, metadata={"description": "store web data"}
            )
            # print(f"[DEBUG]: collection created :{collection}")

        except Exception as e:
            print(f"[DEBUG]: Failed to load store")

        return collection

    # Document adding
    def add_main_content(self, document: list[Any], embeddings: np.array):
        """This will add main document
        Args:
            document:
            embeddings:
        """
        add_document(document, embeddings, self.collection_main)

    def add_page_content(self, document: list[Any], embeddings: np.array):
        """This will add page document
        Args:
            document:
            embeddings:
        """
        add_document(document, embeddings, self.collection_page)

    # Document retrieval
    def retrieve_main_content(self, query: str):
        """This will retrieve main document
        Args:
           query:
        """
        query_embedding = self.embedd.embedd_text([query])[0]
        # print(f"[DEBUG]: Embedded document in to {query_embedding.shape}")

        results = retrieve_document(query_embedding, self.collection_main)

        return results

    def retrieve_page_content(self, query:str,url):
        """This will retrieve main document
        Args:
            query:
        """
        query_embedding = self.embedd.embedd_text([query])[0]
        # print(f"[DEBUG]: Embedded document in to {query_embedding.shape}")

        # print("PRINT URL",url)

        metadata = {
            # "url":{"$in":url}
            "url": url[0]
        }
        # metadata = None
        # print(metadata)
        results = retrieve_document(query_embedding, self.collection_page,n_results=3,metadata=metadata)
        # print(results)
        return results
