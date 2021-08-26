"""Function to generate a new meme from given inputs."""

import MemeEngine
import os
import random
import MemeEngine
import QuoteEngine
import argparse

import QuoteEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(QuoteEngine.Ingestor.parse(f))

        quote = random.choice(quotes)
    elif author is None:
            if body is not None:
                raise Exception('Author Required if Body is Used')
            # Else quote.author already defined by random assignment 
            # since no Body was defined
    else: # Both body and author NOT None
        quote = QuoteEngine.QuoteModel(body, author)

    

    meme = MemeEngine.MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description='Generate a new meme \
        with a given picture and quote')

    parser.add_argument("--path",
                        help="path to an image file to use in the new meme",
                        type=str)
    parser.add_argument("--body",
                        help="quote body to use in the new meme",
                        type=str)
    parser.add_argument("--author",
                        help="author name to use in the new meme",
                        type=str)

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
