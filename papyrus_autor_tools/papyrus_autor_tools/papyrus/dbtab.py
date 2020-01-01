import logging
import logging.config

class Dbtab:
        """Class represents Papyrus Autor DBTAB."""

        def __init__(self, dbtab):
                """Initialize Dbtab class."""
                logging.config.fileConfig('logging.conf')
                self._id = dbtab.get("ID")


        @property
        def id(self):
                return self._id
