"""Strategy Object for Ingesting Quote Files."""
from .IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.TXTIngestor import TXTIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.CSVIngestor import CSVIngestor
from typing import List


class Ingestor(IngestorInterface):
    """Ingestor - Choose which parser is necessary and parse the file."""

    allowed_extensions = ['docx', 'csv', 'txt', 'pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the passed file to extract the quotes.

        Args:
            path:
                path to a file that will be parsed for quotes

        Returns:
            A list of QuoteModel objects containing all the extracted quotes

        Raises:
            FileNotFoundError:
                Thrown if the passed file name isn't found
            Exception:
                Thrown if the passed file doesn't have an extension that can
                be parsed

        """
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
