from typing import List, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import src.load_data as data_loader
import uuid


class Embedding:

    def __init__(self, model_name:str = "all-MiniLM-L6-v2"):
        """This will initialize embedding parameters and call initialize model function
        Args:
          model_name:
        """

        self.model_name = model_name
        self.model = None
        self._initialize_model()

    def _initialize_model(self):
        """This will initialize model"""
        try:
            self.model = SentenceTransformer(self.model_name)
            # print("[DEBUG]: Embedding model loaded")

        except Exception as e:
            print(f"[ERROR]: Failed to load embedding model{e}")

    def chunk_document(self, document,chunk_size:int=1000, chunk_overlap:int = 200):
        """This will split documet to chunks
        Args:
          document:
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            length_function = len,
            separators=["\n\n","\n"," ",""],
        )

        # print("[DEBUG]:TYPE OF DOC",  type(document))

        doc_chunks = text_splitter.split_documents(document)
        # print(f"[DEBUG]: Split document into {len(doc_chunks)}")

        documents = []
        metadatas = []
        ids = []
        # print(doc_chunks)
        for i,doc in enumerate(doc_chunks):
            ids.append(f"doc_{uuid.uuid4().hex[:8]}_{i}")
            metadatas.append(doc.metadata)
            documents.append(doc.page_content)

        data = {"ids": ids, "documents": documents, "metadatas": metadatas}

        # print("[DEBUG]: Completed chunking") 
        return data

    def embedd_text(self,document_text:List[str]):
        """This will embedd the document chunk
        Args:
          document:
        """

        embeddings = self.model.encode(document_text,show_progress_bar=False)
        # print(f"[DEBUG]: Document embedded :{embeddings.shape}")

        return embeddings
