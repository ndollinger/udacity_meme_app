"""Ingestor for PDF Files."""

from QuoteEngine.IngestorInterface import IngestorInterface
from typing import List
from QuoteEngine.QuoteModel import QuoteModel
import random
import subprocess
import os


class PDFIngestor(IngestorInterface):
    """Ingestor Class for PDF Files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a PDF File and return a list of contained quotes.

        Args:
            path:
                path to the PDF containing Quotes

        Returns:
            List of QuoteModel Objects created from the PDF file contents

        Raises:
            Exception:
                Thrown if the file type is not a .pdf file

        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest File Type')

        tmp = f'./tmp_{random.randint(0,100000000)}.txt'
        subprocess.run(['pdftotext', '-layout', path, tmp])
        quotes = []

        with open(tmp, "r") as fp:
            for line in fp:
                if line.strip() != '':
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        os.remove(tmp)
        return quotes
