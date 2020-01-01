import logging
import logging.config

class Fielddef:
        """Class represents Papyrus Autor FIELDDEF."""

        def __init__(self, fielddef):
                """Initialize Fielddef class."""
                logging.config.fileConfig('logging.conf')
                self._name = fielddef.get("NAME")
                self._type = fielddef.get("TYPE")
                self._init = fielddef.get("INIT")
                self._helptext = fielddef.get("HELPTEXT")
                self._not_in_form = fielddef.get("NOT_IN_FORM")
                self._text_allowed = fielddef.get("TEXT_ALLOWED")


        @property
        def name(self):
                return self._name


        @property
        def type(self):
                return self._type


        @property
        def init(self):
                return self._init


        @property
        def helptext(self):
                return self._helptext


        @property
        def not_in_form(self):
                return self._not_in_form


        @property
        def text_allowed(self):
                return self._text_allowed



## <FIELDDEF NAME="ID" TYPE="STRING" INIT="UUID()" HELPTEXT="reserviert, eindeutige Identifikation dieses Datensatzes" NOT_IN_FORM="1"></FIELDDEF>
## <FIELDDEF NAME="Titel" TYPE="STRING" HELPTEXT="Dieser Titel dient der kompletten Angabe über die Quelle"></FIELDDEF>
#<FIELDDEF NAME="Bild" TYPE="PICREF" HELPTEXT="Bild der Quelle"><PIC_ATTR SCALE="256" COPY="1" COPY_PATH="Bilder/"/></FIELDDEF>
#<FIELDDEF NAME="Lokale_Kopie" TYPE="FILEREF" HELPTEXT="reserviertes Feld" NOT_IN_FORM="1"><FILE_REF_ATTR COPY="1" COPY_PATH=""/></FIELDDEF>
## <FIELDDEF NAME="reserviert1" TYPE="STRING" HELPTEXT="reserviert1" NOT_IN_FORM="1"></FIELDDEF>
## <FIELDDEF NAME="reserviert2" TYPE="STRING" NOT_IN_FORM="1"></FIELDDEF>
#<FIELDDEF NAME="Bezugsdatum" TYPE="DATETIME" INIT="NOW()" HELPTEXT="Recherche-Dokument angelegt am (dies Datum wird automatisch erzeugt)"><DATE_ATTR DATE_SEP="." TIME_SEP=":" TIME_FORMAT="1"/></FIELDDEF>
## <FIELDDEF NAME="erschienen" TYPE="STD" HELPTEXT="ursprüngliches Erscheinungsdatum der Quelldatei" NOT_IN_FORM="1" TEXT_ALLOWED="1"></FIELDDEF>
