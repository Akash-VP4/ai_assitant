from src.vector_store import ChromaVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from src.embedd import Embedding
from src.load_data import load_web_text


class Search:

    def __init__(self, vector_store: ChromaVectorStore,embedd = Embedding(), loader = load_web_text()):

        self.embedd = embedd
        self.loader = loader
        self.vector_store = vector_store
        self.llm = None
        self._initialize_llm()

    def _initialize_llm(self):
        """This will load llm"""

        try:
            load_dotenv()
            self.llm = ChatGoogleGenerativeAI(
              model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY")
          )
            print(f"[DEBUG]: Model loaded: {self.llm}")

        except Exception as e:
            print(f"[ERROR]: Failed to load llm: {e}")

    def search(self,query:str):

        # Retrieve from user query
        results = self.vector_store.retrieve_main_content(query)
        # print("RESULTS",results["metadatas"])
        url = results["metadatas"]
        # urls =[]

        # For more than one url
        # for n, metadata in enumerate(results["metadatas"]):
        #     url = metadata
        #     urls.append(url)
        #     print(f"[DEBUG] adding url :{n}, {url}")

        #     # data = self.loader.load_web_content(url)
        #     # chunks = self.embedd.chunk_document(data)
        #     # embedded_chunk = self.embedd.embedd_text(chunks["documents"])
        #     # self.vector_store.add_page_content(chunks, embedded_chunk)

        # # url  = results['metadatas'][0][0]["url"]

        
        print(f"[DEBUG]: url extracted: {results}")
        page_results = self.vector_store.retrieve_page_content(query,url)
       
        if not page_results:
            print("[DEBUG]: Adding page to collection")
            data = self.loader.load_web_content(url[0])
            chunks = self.embedd.chunk_document(data)
            embedded_chunk = self.embedd.embedd_text(chunks["documents"])
            self.vector_store.add_page_content(chunks, embedded_chunk)

            page_results = self.vector_store.retrieve_page_content(
                query, url
            )

        context: str = (
            "\n\n".join([doc for doc in page_results["documents"]]) if results else ""
        )
        print(f"[DEBUG]:  Context extracted")
        
        if not context:
            return "No relevent content found!"
        
        prompt = f"""Answer for the following question using the context given below
         \n context:{context}
         \n question: {query}
        """

        response = self.llm.invoke([prompt])

        return {"answer":response.content,"url":url[0][:-2]}
