from QuoteEngine.IngestorInterface import IngestorInterface
from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
    
