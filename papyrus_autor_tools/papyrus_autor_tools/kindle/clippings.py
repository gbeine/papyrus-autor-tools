import logging
import logging.config

from papyrus_autor_tools.kindle import clipping

class Clippings:
        """Class for handling the Kindle My Clippings file."""

        def __init__(self, path, filename):
                """Initialize Clippings class."""
                logging.config.fileConfig('logging.conf')
                self._path = path
                self._file = filename
                self._clippings = []


        def open(self):
                """Read the file."""
                filename = self._path + "/" + self._file
                logging.debug("Reading %s", filename)
                self._parse(filename)


        @property
        def clippings(self):
                return self._clippings


        def _parse(self, filename):
                with open(filename, "r", encoding="utf-8", newline="\r\n") as infile:
                        i = 0
                        for text in infile:
                                text = text.strip('\r\n')
                                if text == "==========":
                                        continue
                                if i == 0:
                                        title_author = text
                                        i += 1
                                elif i == 1:
                                        reference = text
                                        i += 1
                                elif i == 2:
                                        i += 1
                                elif i == 3:
                                        citation = text
                                        if len(text) > 0:
                                                self._clippings.append(clipping.Clipping(title_author, reference, citation))
                                        i = 0


