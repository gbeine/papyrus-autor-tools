import logging
import logging.config

class Dbtabdef:
        """Class represents Papyrus Autor DBTABDEF."""

        def __init__(self, dbtabdef):
                """Initialize Dbtabdef class."""
                logging.config.fileConfig('logging.conf')
                self._id = dbtabdef.get("ID")


        @property
        def id(self):
                return self._id
