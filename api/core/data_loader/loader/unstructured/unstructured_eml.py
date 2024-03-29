import base64
import logging
from typing import List

from bs4 import BeautifulSoup
from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document

logger = logging.getLogger(__name__)


class UnstructuredEmailLoader(BaseLoader):
    """Load msg files.
    Args:
        file_path: Path to the file to load.
    """

    def __init__(
        self,
        file_path: str,
        api_url: str,
    ):
        """Initialize with file path."""
        self._file_path = file_path
        self._api_url = api_url

    def load(self) -> List[Document]:
        from unstructured.partition.email import partition_email
        elements = partition_email(filename=self._file_path, api_url=self._api_url)

        # noinspection PyBroadException
        try:
            for element in elements:
                element_text = element.text.strip()

                padding_needed = 4 - len(element_text) % 4
                element_text += '=' * padding_needed

                element_decode = base64.b64decode(element_text)
                soup = BeautifulSoup(element_decode.decode('utf-8'), 'html.parser')
                element.text = soup.get_text()
        except Exception:
            pass

        from unstructured.chunking.title import chunk_by_title
        chunks = chunk_by_title(elements, max_characters=2000, combine_text_under_n_chars=0)
        documents = []
        for chunk in chunks:
            text = chunk.text.strip()
            documents.append(Document(page_content=text))
        return documents
