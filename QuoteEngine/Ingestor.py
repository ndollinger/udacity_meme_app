from .IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.TXTIngestor import TXTIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from typing import List

class Ingestor(IngestorInterface):

    allowed_extensions = ['docx', 'csv', 'txt', 'pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        file_type = IngestorInterface.file_type(path)
        if file_type == 'csv':
            return CSVIngestor.parse(path)
        elif file_type == 'docx':
            return DocxIngestor.parse(path)
        elif file_type == 'txt':
            return TXTIngestor.parse(path)
        elif file_type == 'pdf':
            return PDFIngestor.parse(path)
        else:
            raise Exception('Cannot Ingest File type')