from src.load_data import load_web_text
from src.embedd import Embedding
from src.vector_store import ChromaVectorStore
from src.search import Search


def main():
    print("Hello from rag-langchain-assistent!")


if __name__ == "__main__":
    # loader = load_web_text()
    # data = loader.load_llms_text("https://docs.langchain.com/llms.txt")
    # # print(data)

    # text = data["documents"]
    # embedd = Embedding().embedd_text(data['documents'])
    # # print(embedd)

    # db = ChromaVectorStore()
    # db.add_main_content(data,embedd)

    # # testing pagewise
    loader = load_web_text()
    # data = loader.load_web_content(
    #     "https://docs.langchain.com/langsmith/agent-builder.md"
    # )
    embedd = Embedding()
    # chunks = embedd.chunk_document(data)
    # print(type(chunks["documents"][0]))
    # embedded_chunk = embedd.embedd_text(chunks["documents"])

    db = ChromaVectorStore()
    # db.add_page_content(chunks, embedded_chunk)

    # Retrieve from user query
    # results = db.retrieve_main_content("what is aai agents?")
    # print(results)

    # for n, metadata in enumerate(results["metadatas"][0]):
    #     url = metadata["url"]
    #     print(f"[DEBUG] retrived result :{n} ,{url}")

    #     data = loader.load_web_content(url)
    #     chunks = embedd.chunk_document(data)
    #     embedded_chunk = embedd.embedd_text(chunks["documents"])
    #     db.add_page_content(chunks, embedded_chunk)

    # page_results = db.retrieve_page_content("what is aai agents?")
    # print(page_results)

    sr = Search(db)

    print("Hi, How can i help you? enter 'exit' for quit")
    while True:
        user_query = input("Enter your query:")
        res = sr.search(user_query)
        print("thinking..")
        if user_query == "exit":
            break

        print(res["answer"])
        print("link :", res["url"])
