# Papyrus Autor Tools
My toolchain for managing the Papyrus Autor references database.

## What are the tools doing?

All tools are import only to Papyrus Autor.
The fetch data from different sources where I get my citations from and write them into a Papyrus Autor reference database.

- zotero-import: import reference data from Zotero
- pocketbook-import: import quotations from PocketBook e-book readers
- kindle-import: import clippings from Kindle My Clippings.txt
- cr3-import: import clippings from Cool Reader 3 (from PocketBook)

## Install

- clone the git repository
- ensure to have Python 3 with venv installed
- run the ```install``` script in the local directory

## Configuration

- copy ```papyrus-autor.yaml.example```
- configure as you like
- use ```<<HOME>>``` as a placeholder for your home directory in all options named with 'path'

### Papyrus Autor configuration

Papyrus Autor requires two configuration options.

```reference_path``` is the directory where your database is located.
```reference_database``` is the database file, it usually ends with ```.pb```

```
papyrus:
    reference_path: <<HOME>>/Publishing/Research
    reference_database: Research.pb
```
### Zotero configuration

Zotero requires two configuration options.

```zotero_path``` is the directory where your database is located.
```zotero_database``` is the database file. Do not change it.

```
zotero:
    zotero_path: <<HOME>>/Zotero
    zotero_database: zotero.sqlite
```

### Kindle configuration

Kindle requires three configuration options.

```kindle_path``` is the directory where your Kindle will be mounted.
```kindle_file``` is the Kindle's clippings file. It is usually 'My Clippings.txt'
```kindle_lang``` is the Kindle's clippings language. Currently, only German (DE) is supported.

```
kindle:
    kindle_path: <<HOME>>/Cloud/nextcloud.office/Kindle
    kindle_file: My Clippings.txt
    kindle_lang: DE
```
### PocketBook configuration

PocketBook requires three configuration options.

```pocketbook_path``` is the directory where your PocketBook will be mounted.
```pocketbook_type``` is the PocketBook type. Currently only 'PB632' and 'PB1040' are tested
```pocketbook_database``` is the PocketBook's book database.  Do not change it.

```
pocketbook:
    pocketbook_path: /Volumes
    pocketbook_type: PB632
    pocketbook_database: /system/config/books.db
```
## Plans

- Export BibTex entries for all references
- Write a one-for-all import script
