"""Flask app to serve generated memes."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor
from PIL import Image, UnidentifiedImageError
from io import BytesIO

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []

    # Walking a directory tree and printing the names of
    # the directories and files
    for dirpath, dirnames, files in os.walk(images_path):
        for file_name in files:  # Should I actually check the file type?
            imgs.append(f'{dirpath}{file_name}')

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    img_url = request.form['image_url']
    temp_image = "temp_" + img_url.split('/')[-1]
    try:
        response = requests.get(img_url)
    except Exception as e:
        app.logger.error(f'Error while fetching {img_url}: {str(e)}') 
        return render_template('meme_generator_error.html')

    try:
        i = Image.open(BytesIO(response.content))
    except UnidentifiedImageError as uie:
        app.logger.error(f'UnidentifedImage Error when opening {img_url}: {str(uie)}')
        return render_template('meme_generator_error.html')
    
    try:
        i.save(temp_image)
    except Exception as e:
        app.logger.error(f'Failed to save temp {temp_image}: {str(e)}')
        return render_template('meme_generator_error.html')


    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    body = request.form['body'] or "You forgot a quote"
    author = request.form['author'] or "You Forgot an Author"
    path = meme.make_meme(temp_image, body, author)

    # 3. Remove the temporary saved image.
    os.remove(temp_image)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
