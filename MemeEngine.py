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
        tmp_image_path = ''

        # Load the image
        with open(img_path, "rb") as img_reader:
            im = Image.open(img_reader)

            # resize to a max width "width" and proportional to height
            if im.width > width:
                (im_width, im_height) = im.size
                image_proportion = im_height/im_width
                im = im.resize((width, int(width*image_proportion)))

            # Add Quote to the image (TODO: Check calling conventions here)
            self.__draw_quote_on_img(im, text, author)
 
            # save the image
            tmp_image_path = f'{self.temp_dir}/tmp_{random.randint(0,100000000)}.jpg'
            im.save(tmp_image_path)

        # return the path to the image
        return tmp_image_path

    def __draw_quote_on_img(self, image, text, author):
        """Draw given quote on an image.

        Draw give quote and author name on pass PIL.Image
        resize the text as necessary to fit on the image

        Parameters:
            image:
                PIL.Image to draw text on
            text:
                Body of the quote
            author:
                Author of the quote

        Returns:
            Nothing

        Raises:
            TBD
        """
        quote_str = f'{text} - {author}'
        # TODO: where should this be drawn?
        # TODO: Modify the color of the text to make more readable?
        draw = ImageDraw.Draw(image)
        
        # Make the font size fit the image
        # No greater than 25 point though
        font_size = 25
        text_height, text_width = image.height, image.width
        while (text_width >= image.width or text_height >= image.height) and font_size > 1:
            font = ImageFont.truetype(
                "./_data/fonts/Laffayette_Comic_Pro.ttf", font_size)
            (text_width, text_height) = font.getsize(quote_str)
            font_size -= 1 

        draw.text((10, 10), quote_str,
                      fill=(255, 255, 255, 255), 
                      font=font)
