from QuoteEngine.Ingestor import Ingestor


def main():
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
               './_data/DogQuotes/DogQuotesDOCX.docx',
               './_data/DogQuotes/DogQuotesPDF.pdf',
               './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    #quotes.extend(Ingestor.parse('_data/DogQuotes/DogQuotesTXT.txt'))

    for file in quote_files:
        new_quotes = Ingestor.parse(file)
        quotes.extend(new_quotes)

    print(quotes)

if __name__ == "__main__":
    main()