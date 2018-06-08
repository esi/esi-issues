# Conversions
## Intoduction

Originally, the SDE was provided solely as an MS SQL server backup file. As the SDE is commonly used in environments where MS SQL is not available or would be overkill, a number of people maintain conversion routines and copies, to make it available in a more useful format.

As more formats were introduced, containing extra data, these routines were expanded to bring the data back into a single format.

As the various methods for conversion result in differing versions, with different layouts of data, conversions will be listed by the primary maintainer.

## [EVE SDE Database Builder - by Zifrian](https://forums.eveonline.com/default.aspx?g=posts&t=500859)
EVE SDE Database Builder is a Windows application that lets users import the SDE yaml files into MS Access, MS SQL Server, Comma Separated Values, Semi-colon Separated Values, MySQL, PostgreSQL, and SQLite. Additionally, users can customize the import by language type and selecting specific SDE yaml files to import or ignore.

Main links for the application:
* [Screenshot of the program](http://i.imgur.com/iQIyUrw.png)
* [Binaries for installing the program](https://github.com/EVEIPH/EVE-SDE-Database-Builder/raw/master/Latest%20Files/EVE%20SDE%20Database%20Builder%20Install.zip)
* [SQL Schema used](https://github.com/EVEIPH/EVE-SDE-Database-Builder/blob/master/Latest%20Files/EVESDEDB_Schema.sql)
* [Github for the code](https://github.com/EVEIPH/EVE-SDE-Database-Builder)

## [Desmont McCallock](https://forums.eveonline.com/profile/Desmont%20McCallock)

[Conversion Tool](https://forums.eveonline.com/default.aspx?g=posts&m=6168357)

Desmont provides a tool to run on Windows, to merge the other data back into the SQL Server SDE, and to convert into a variety of formats, either at full database, or individual tables.

* SQL Server
* MySQL
* Postgres
* MS Access
* SQLite
* CSV

This tool converts to a format close to the SDE as it was before CCP changed how it was produced -splitting it sqlserver, yaml and sqlite files- with blueprint information going into ramTypeRequirements. As such it should be more compatible with some older tools.

## [Steve Ronuken - Fuzzwork Enterprises](https://www.fuzzwork.co.uk/dump/)

Steve provides conversions of the SDE for download, in the following formats:

* SQL Server
* MySQL (both [full database](https://www.fuzzwork.co.uk/dump/mysql-latest.tar.bz2) and [single table](https://www.fuzzwork.co.uk/dump/latest/))
* [Postgres](https://www.fuzzwork.co.uk/dump/postgres-latest.dmp.bz2) (both public schema, and evetools schema)
* [SQLite](https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2)
* [CSV/XLS](https://www.fuzzwork.co.uk/dump/latest/) (depending on row counts)

.bz2 files can be unzipped with 7zip, on Windows.
Historical copies are kept available. When data is migrated into alternate formats, it's generally copied back into the old table format, but not always. The industry data, for example, is in a number of new industryActivity tables. While allowing for greater flexibility, this can break some older tools.

Conversion is performed with [https://github.com/fuzzysteve/yamlloader](https://github.com/fuzzysteve/yamlloader) which can target any database which SQLAlchemy can work with.
