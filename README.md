# Medieval fairs in Germany crawler

Crawling event dates of medieval fairs in Germany (from Marktkalendarium) for database storage

## Description

The goal of the present project is to download, parse and store event dates provided by [Marktkalendarium](http://www.marktkalendarium.de/) for later usage.

## Crwaling raw data for testing purpose

### Pre PHP era

```bash
# Event years from 2004 until 2008

for YEAR in $(seq 2004 2008);
do
  curl --output "maerkte${YEAR}.html" \
    "http://www.marktkalendarium.de/maerkte${YEAR}.htm";
done
```

### PHP era

```bash
# Event years since 2009

for YEAR in $(seq 2009 $(($(date +%Y) + 1)));
do
  curl --output "maerkte${YEAR}.html" \
    "http://www.marktkalendarium.de/maerkte${YEAR}.php?datenbereich=alle";
done
```
