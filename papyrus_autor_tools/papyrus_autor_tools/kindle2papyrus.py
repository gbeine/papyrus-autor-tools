from papyrus_autor_tools import config
from papyrus_autor_tools.papyrus import references
from papyrus_autor_tools.kindle import clippings
from papyrus_autor_tools.converter import kindle2papyrus

def main():
        cfg = config.Config()
        cfg.read()
        database = references.References(cfg.papyrus_path, cfg.papyrus_database)
        database.open()
        kindle = clippings.Clippings(cfg.kindle_path, cfg.kindle_file)
        kindle.open()
        items = []
        for item in kindle.clippings:
                k2p = kindle2papyrus.Kindle2papyrus(item)
                items.append(k2p.r)
        # TODO add items to database
