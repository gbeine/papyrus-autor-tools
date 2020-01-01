import logging
import logging.config

class Report:
        """Class represents Papyrus Autor REPORT."""

        def __init__(self, report):
                """Initialize Report class."""
                logging.config.fileConfig('logging.conf')
                self._name = report.get("NAME")
                self._page_break = report.get("PAGE_BREAK")
                self._default_report = report.get("DEFAULT_REPORT")
                self._selected = papbase.get("SELECTED")


        @property
        def name(self):
                return self._name


        @property
        def page_break(self):
                return self._page_break


        @property
        def default_report(self):
                return self._default_report


        @property
        def selected(self):
                return self._selected
