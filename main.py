from src.load_data import load_web_text
from src.embedd import Embedding
from src.vector_store import ChromaVectorStore
from src.search import Search


if __name__ == "__main__":

    # loader = load_web_text()
    # data = loader.load_llms_text("https://docs.langchain.com/llms.txt")
    # # print(data)

    # text = data["documents"]
    # embedd = Embedding().embedd_text(data['documents'])
    # # print(embedd)

    # db = ChromaVectorStore()
    # db.add_main_content(data,embedd)

    print("db..")
    db = ChromaVectorStore()
    print("search..")
    sr = Search(db)

    print("starting loop")

    print("Hi, How can i help you? enter 'exit' for quit")
    while True:
        user_query = input("Enter your query: ")

        if user_query.lower() == "exit":
            print("exiting..")
            break 

        res = sr.search(user_query)
        print("thinking..")
        print(res["answer"])
        print("link :", res["url"])
