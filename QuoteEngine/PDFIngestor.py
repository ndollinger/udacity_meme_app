from QuoteEngine.IngestorInterface import IngestorInterface
from typing import List
from QuoteEngine.QuoteModel import QuoteModel
import random
import subprocess
import os

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest File Type')
        
        tmp = f'./tmp_{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file_ref = open(tmp, "r")
        quotes = []
        
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
                
        file_ref.close()
        os.remove(tmp)
        return quotes