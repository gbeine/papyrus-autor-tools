import yaml
import logging
import logging.config

from os.path import expanduser

class Config:
        """Class for parsing papyrus-autor.yaml."""

        def __init__(self):
                """Initialize Config class."""
                logging.config.fileConfig('logging.conf')
                self._papyrus = {}
                self._zotero = {}
                self._pocketbook = {}
                self._home = expanduser("~")


        def read(self, file='papyrus-autor.yaml'):
                """Read config."""
                logging.debug("Reading %s", file)
                try:
                        with open(file, 'r') as filehandle:
                                config = yaml.load(filehandle, Loader=yaml.FullLoader)
                                self._parse_papyrus(config)
                                self._parse_kindle(config)
                except FileNotFoundError as ex:
                        logging.error("Error while reading %s: %s", file, ex)

        @property
        def papyrus_path(self):
                return self._papyrus["reference_path"]


        @property
        def papyrus_database(self):
                return self._papyrus["reference_database"]


        @property
        def kindle_path(self):
                return self._kindle["kindle_path"]


        @property
        def kindle_file(self):
                return self._kindle["kindle_file"]


        def _parse_papyrus(self, config):
                """Parse the Papyrus Autor section of papyrus-autor.yaml."""
                if "papyrus" in config:
                        self._papyrus = config["papyrus"]
                if not "reference_path" in self._papyrus:
                        raise ValueError("Path to reference database not set")
                if not "reference_database" in self._papyrus:
                        raise ValueError("Name of reference database not set")
                self._papyrus["reference_path"] = self._papyrus["reference_path"].replace("<<HOME>>", self._home)


        def _parse_kindle(self, config):
                """Parse the Kindle section of papyrus-autor.yaml."""
                if "kindle" in config:
                        self._kindle = config["kindle"]
                if not "kindle_path" in self._kindle:
                        raise ValueError("Path to kindle not set")
                if not "kindle_file" in self._kindle:
                        raise ValueError("Name of kindle clippings file not set")
                self._kindle["kindle_path"] = self._kindle["kindle_path"].replace("<<HOME>>", self._home)
