from src.load_data import load_web_text
from src.embedd import Embedding
from src.vector_store import ChromaVectorStore


def main():
    print("Hello from rag-langchain-assistent!")


if __name__ == "__main__":
    # loader = load_web_text()
    # data = loader.load_llms_text("https://docs.langchain.com/llms.txt")
    # print(data)

    # # text = [doc.page_content for doc in data]
    # # embedd  = Embedding.embedd_text(data['documents'])
    # # print(text)
    # embedd = Embedding().embedd_text(data['documents'])
    # print(embedd)

    # db = ChromaVectorStore()
    # db.add_document(data,embedd)

    # testing pagewise
    loader = load_web_text()
    data = loader.load_web_content(
        "https://docs.langchain.com/langsmith/agent-builder.md"
    )
    embedd = Embedding()
    chunks = embedd.chunk_document(data)
    print(type(chunks["documents"][0]))
    embedded_chunk = embedd.embedd_text(chunks["documents"])

    db = ChromaVectorStore()
    db.add_page_content(chunks, embedded_chunk)
