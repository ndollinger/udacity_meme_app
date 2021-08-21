"""Ingestor for CSV Files."""

from QuoteEngine.IngestorInterface import IngestorInterface
from typing import List
from QuoteEngine.QuoteModel import QuoteModel
import csv


class CSVIngestor(IngestorInterface):
    """Quote Ingestor class for CSV Files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a CSV and return a list of contained quotes.

        Args:
            path:
                path to the CSV containing Quotes

        Returns:
            List of QuoteModel Objects created from the csv file contents

        Raises:
            Exception:
                Thrown if the file type is not a .csv file

        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest File type')

        quotes = []

        with open(path, 'r') as infile:
            reader = csv.DictReader(infile)
            for elem in reader:
                new_quote = QuoteModel(elem['body'], elem['author'])
                quotes.append(new_quote)
        return quotes
