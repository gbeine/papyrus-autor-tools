import logging
import logging.config

class Papbase:
        """Class represents Papyrus Autor PAPBASE."""

        def __init__(self, papbase):
                """Initialize Papbase class."""
                logging.config.fileConfig('logging.conf')
                self._oldest_reader = papbase.get("OLDEST_READER")
                self._oldest_writer = papbase.get("OLDEST_WRITER")
                self._reorg_count = papbase.get("REORG_COUNT")
                self._reorg_time = papbase.get("REORG_TIME")
                self._version = papbase.get("VERSION")


        @property
        def oldest_reader(self):
                return self._oldest_reader


        @property
        def oldest_writer(self):
                return self._oldest_writer


        @property
        def reorg_count(self):
                return self._reorg_count


        @property
        def reorg_time(self):
                return self._reorg_time


        @property
        def version(self):
                return self._version
