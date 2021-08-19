from QuoteEngine.IngestorInterface import IngestorInterface
from typing import List
from QuoteEngine.QuoteModel import QuoteModel
import csv

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest File type')
            
        quotes = []

        with open(path, 'r') as infile:
            reader = csv.DictReader(infile)
            for elem in reader:
                new_quote = QuoteModel(elem['body'], elem['author'])
                quotes.append(new_quote)
        return quotes