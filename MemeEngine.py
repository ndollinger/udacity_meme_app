"""MemeEngine and related code."""
from PIL import Image, ImageDraw, ImageFont
import random
import os

class MemeEngine:
    """Class that creates Memes."""
    
    temp_dir = "."

    def __init__(self, temp_dir: str):
        """Generate a MemeEngine."""
        # Personally I'm not sure this really needs to be more than 
        # just a static method, note sure why it needs to be own 
        # class and the temp dir thing is weird
        self.temp_dir = temp_dir
        if not os.path.exists(self.temp_dir): # This could be abused
            os.makedirs(self.temp_dir)


    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Generate a new meme by mashing up quote and image.

        Args:
            img_path:
                path to an image to be used to create the meme
            text:
                body of the quote to be used to create the meme
            author:
                name of the author of the quote
            width:
                max size of the generated image (in px). If image is smaller
                   than this, it will not be resized

        Returns:
            A string that is the path to the generated meme

        Raises:
            FileNotFoundError:
                Thrown if the image to be used to create the meme isn't foudnd

        """
        tmp_image = ''

        # Load the image
        with open(img_path, "rb") as img_reader:
            im = Image.open(img_reader)

            # resize to a max width "width" and proportional to height
            if im.width > width:
                (im_width, im_height) = im.size
                image_proportion = im_height//im_width
                im = im.resize((width, width*image_proportion))

            # Add Quote to the image 
            # TODO: where should this be drawn?
            # TODO: Modify the color of the text to make more readable?
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype(
                "./_data/fonts/Laffayette_Comic_Pro.ttf", 25)
            draw.text((10, 10), f'{text} - {author}',
                      fill=(255, 255, 255, 255), font=font)
            # save the image
            tmp_image = f'{self.temp_dir}/tmp_{random.randint(0,100000000)}.jpg'
            im.save(tmp_image)

        # return the path to the image
        return tmp_image
