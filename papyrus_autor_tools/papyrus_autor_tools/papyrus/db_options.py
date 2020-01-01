import logging
import logging.config

class Dboptions:
        """Class represents Papyrus Autor DB_OPTIONS."""

        def __init__(self, db_options):
                """Initialize Dboptions class."""
                logging.config.fileConfig('logging.conf')
                self._index = db_options.get("INDEX")
                self._index_phonetic = db_options.get("INDEX_PHONETIC")
                self._delayed_save = db_options.get("DELAYED_SAVE")
                self._avoid_sort = db_options.get("AVOID_SORT")
                self._main_ask = db_options.get("MAIN_ASK")
                self._main_no_reorg = db_options.get("MAIN_NO_REORG")
                self._overwrite_backup = db_options.get("OVERWRITE_BACKUP")
                self._make_backups = db_options.get("MAKE_BACKUPS")
                self._nbackups = db_options.get("NBACKUPS")
                self._backup_use_path = db_options.get("BACKUP_USE_PATH")
                self._backup_path = db_options.get("BACKUP_PATH")
                self._multiuser = db_options.get("MULTIUSER")
                self._login_required = db_options.get("LOGIN_REQUIRED")
                self._special_type = db_options.get("SPECIAL_TYPE")
                self._lang = db_options.get("LANG")


        @property
        def index(self):
                return self._index


        @property
        def index_phonetic(self):
                return self._index_phonetic


        @property
        def delayed_save(self):
                return self._delayed_save


        @property
        def avoid_sort(self):
                return self._avoid_sort


        @property
        def main_ask(self):
                return self._main_ask


        @property
        def main_no_reorg(self):
                return self._main_no_reorg


        @property
        def overwrite_backup(self):
                return self._overwrite_backup


        @property
        def make_backups(self):
                return self._make_backups


        @property
        def nbackups(self):
                return self._nbackups


        @property
        def backup_use_path(self):
                return self._backup_use_path


        @property
        def backup_path(self):
                return self._backup_path


        @property
        def multiuser(self):
                return self._multiuser


        @property
        def login_required(self):
                return self._login_required


        @property
        def special_type(self):
                return self._special_type


        @property
        def lang(self):
                return self._lang
