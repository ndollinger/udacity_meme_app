"""Module containing QuoteModel class."""


class QuoteModel():
    """Quote that consists of a quote body string and an author string.

    Attributes:
        body - the quote itself
        author - the name of the quote's author
    """

    body = ''
    author = ''

    def __init__(self, body: str, name: str):
        """Initialize a Quote, check inputs.

        replaces an empty name with "unknown"
        """
        self.author = name
        if not name:
            self.author = "unknown"
        self.body = body

    def __str__(self):
        """Print the quote in a 'quote' format."""
        return f'{self.body} - {self.author}'
