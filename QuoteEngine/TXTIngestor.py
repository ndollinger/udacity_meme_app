"""Ingest for Text Files."""
from QuoteEngine.IngestorInterface import IngestorInterface
from typing import List
from QuoteEngine.QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Ingestor Class for Text Files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a txt File and return a list of contained quotes.

        Args:
            path:
                path to the txt containing Quotes

        Returns:
            List of QuoteModel Objects created from the txt file contents

        Raises:
            Exception:
                Thrown if the file type is not a .txt file

        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest File type')

        quotes = []

        with open(path, "r") as f:
            for line in f:
                parse = line.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
