import logging
import logging.config

class R:
        """Class represents Papyrus Autor R."""

        def __init__(self, r = None):
                """Initialize R class."""
                logging.config.fileConfig('logging.conf')
                if r is not None:
                        self._content = r.text

        @property
        def author(self):
                return self._author
        @author.setter
        def author(self, value):
                self._author = value
