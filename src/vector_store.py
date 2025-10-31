import os
import chromadb
from typing import List, Any
import numpy as np
from src.embedd import Embedding



class ChromaVectorStore:

    def __init__(self,embedding: Embedding,collection_name="web_data",persistent_directory="../db"):
        
        self.embedd = Embedding 
        self.persistent_directory = persistent_directory
        self.collection_name = collection_name
        self.client = None
        self.collection = None
        self._initialize_store()

    def _initialize_store(self):
        """This will initialize store"""

        try:
            os.makedirs(self.persistent_directory,exist_ok=True)
            self.client = chromadb.PersistentClient(path=self.persistent_directory)
            self.collection = self.client.get_or_create_collection(
                name= self.collection_name,
                metadata={"description":"store web data"}
            )
            print(f"[DEBUG]: collection created :{self.collection}")

        except Exception as e:
            print(f"[DEBUG]: Failed to load")

        def add_document(self,document:list[Any],embeddings:np.array):
            """This will add document"""
        


      