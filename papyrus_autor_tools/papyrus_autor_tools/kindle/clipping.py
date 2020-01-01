import logging
import logging.config

class Clipping:
        """Class for handling the Kindle clippings."""

        def __init__(self, title_author, reference, citation):
                """Initialize Clipping class."""
                logging.config.fileConfig('logging.conf')
                self._parse_title_author(title_author)
                self._parse_reference(reference)
                self._parse_citation(citation)


        @property
        def author(self):
                return self._author


        @property
        def title(self):
                return self._title


        @property
        def position(self):
                return self._position


        @property
        def datetime(self):
                return self._datetime


        @property
        def citation(self):
                return self._citation


        def _parse_title_author(self, title_author):
                self._author = title_author[title_author.find("(")+1:title_author.find(")")]
                self._title = title_author[0:title_author.find("(")-1]


        def _parse_reference(self, reference):
                # 22 and 17 are for German "My Clippings.txt"
                # Support for other languges may be required some day...
                self._position = reference[22:reference.rfind("|")-1]
                reference = reference[reference.rfind("|")+17:]
                self._datetime = reference[reference.rfind(",")+2:]


        def _parse_citation(self, citation):
                self._citation = citation
