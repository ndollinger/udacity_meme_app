"""Ingestor for docx Files."""

from QuoteEngine.IngestorInterface import IngestorInterface
from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    """Quote Ingestor class for docx Files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a Docx File and return a list of contained quotes.

        Args:
            path:
                path to the Docx containing Quotes

        Returns:
            List of QuoteModel Objects created from the docx file contents

        Raises:
            Exception:
                Thrown if the file type is not a .docx file

        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest File type')

        quotes = []
        document = Document(path)

        for paragraph in document.paragraphs:
            if paragraph.text != '':
                parse = paragraph.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        return quotes
