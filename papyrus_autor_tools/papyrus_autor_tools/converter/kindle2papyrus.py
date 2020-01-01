import logging
import logging.config

from papyrus_autor_tools.papyrus import r

class Kindle2papyrus:
        """Class for converting Kindle clippings into Papyrus Autor references."""

        def __init__(self, clipping):
                """Initialize Kindle2papyrus class."""
                logging.config.fileConfig('logging.conf')
                self._clipping = clipping


        @property
        def r(self):
                self._convert()
                return self._r


        def _convert(self):
                self._r = r.R()
                self._r.author = self._clipping.author
