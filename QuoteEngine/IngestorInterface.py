"""Abstract Base Class for Ingestors."""

from abc import ABC, abstractmethod
from typing import List
from QuoteEngine import QuoteModel


class IngestorInterface(ABC):
    """Abstract Base Class for Ingestors."""

    allowed_extensions = []

    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        """Parse input files for quotes."""
        pass

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return True if the pass path can be parsed by the object."""
        ext = IngestorInterface.file_type(path)
        return ext in cls.allowed_extensions

    @staticmethod
    def file_type(path: str) -> str:
        """Return a file type for a given path."""
        return path.split('.')[-1]
