import requests

# import validator
from typing import List, Any
import re
from langchain_core.documents import Document


class load_web_text:

    def __init__(self):
        self.web_contents = None

    def load_llms_text(self, url) -> List[Any]:
        """Fetch data from web

        Args:
          web_url: url to the website
        """

        try:
            data = requests.get(url)
            self.web_contents = data.text.splitlines()
            print("[DEGUB]: Web data extracted")

        except Exception as e:
            print(f"[ERROR]: Failed to fetch web data: {e}")

        ids = []
        page_urls = []
        page_content = []

        documents = []

        for id, line in enumerate(self.web_contents, 1):
            pattern_url = r"\((https?://[^\s)]+)\)"

            url = re.search(pattern_url, line)
            if url:
                url = url.group(1)
                url_title = re.sub(pattern_url, "", line)[1:]

                # adding to list
                ids.append(str(id))
                page_urls.append(url)
                page_content.append(url_title)

                # doc = Document(ids=id, page_content=url_title, metadata={"url": url})

                # print(
                #     f"[DEBUG]: Adding to list URL STATUS: {validators.url(url)} title: {url_title} and url: {url}"
                # )

                # documents.append(doc)

        documents = {"ids": ids, "documents": page_content, "metadatas": page_urls}

        return documents
