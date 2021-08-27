# Meme Generator

Generate Memes which are a combination of quotes and images.

## QuoteEngine

This is the module that handles ingesting quotes from various sources and creating new quotes.

### QuoteModel

An object that holds Quotes

### Ingestor(s)

The `Ingestor` class implements the `IngestorInterface` Abstract Base class and is a strategy object that determines what kind of Ingestor is needed based on the the passed file.  The following types of Ingestors are supported

#### PDFIngestor

Parse and create a list of QuoteModels from PDF Files.  Requires the `pdftotext` command line utility to be installed.

```text
body - author
```

#### CSVIngestor

Parse and create a list of QuoteModels from CSV Files.  

Quotes should be in the format:

```csv
body, author
```

**NOTE:** the grading rubric suggests to use the Pandas CSV functionality, but since the project doesn't use any other Pandas functionality, I just used the `csv` module which I think is more appropriate here

#### TXTIngestor

Parse and create a list of QuoteModels from Txt Files.

Quotes should be in the format:

```text
body - author
```

#### DOCXIngestor

Parse and create a list of QuoteModels from .docx files.

Quotes should be in the format:

```text
body - author
```

## MemeEngine

This is the module that actually creates the memes by marrying the Quotes from the QuoteEngine and images.  Generated Memes are saved to disk from where they can later be recalled.

---

## Application Entry Points

`QuoteEngine` and `MemeEngine` are combined to create a meme generator.  The meme generator can be used either as a command line utility or as a `flask` application.

### meme.py

Provides a command line interface that allows users to pass paths to quotes and images which are used to create a meme.  

### Flask application

The Flask Application is contained in `app.py`.  Running this flask application creates a web interface for viewing random memes and allowing users to create their own memes.
