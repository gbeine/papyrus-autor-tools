import logging
import logging.config
import xml.etree.ElementTree as ElementTree

from papyrus_autor_tools.papyrus import papbase
from papyrus_autor_tools.papyrus import pbheader
from papyrus_autor_tools.papyrus import db_options
from papyrus_autor_tools.papyrus import dbtabdef
from papyrus_autor_tools.papyrus import fielddef
from papyrus_autor_tools.papyrus import report
from papyrus_autor_tools.papyrus import dbtab
from papyrus_autor_tools.papyrus import r

class References:
        """Class for handling with the Papyrus Autor references database."""

        def __init__(self, path, database):
                """Initialize References class."""
                logging.config.fileConfig('logging.conf')
                self._path = path
                self._database = database


        def open(self):
                """Read the existing database."""
                filename = self._path + "/" + self._database
                logging.debug("Reading %s", filename)
                root = ElementTree.parse(filename).getroot()
                self._parse(root)


        def _parse(self, root):
                elements = root.findall(".")
                self._papbase = papbase.Papbase(elements[0])
                self._pbheader = pbheader.Pbheader()
                elements = root.findall(".//DB_OPTIONS")
                self._db_options = db_options.Dboptions(elements[0])
                elements = root.findall(".//DBTABDEF")
                self._dbtabdef = dbtabdef.Dbtabdef(elements[0])
                elements = root.findall(".//FIELDDEF")
                self._fielddefs = []
                for element in elements:
                        self._fielddefs.append(fielddef.Fielddef(element))
                elements = root.findall(".//REPORT")
                if elements:
                    self._report = report.Report(elements[0])
                elements = root.findall(".//DBTAB")
                self._dbtab = dbtab.Dbtab(elements[0])
                elements = root.findall(".//R")
                self._rs = []
                for element in elements:
                        self._rs.append(r.R(element))
