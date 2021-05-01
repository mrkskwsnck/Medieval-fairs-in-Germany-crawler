#!/usr/bin/env python3

from datetime import datetime
import os
from bs4 import BeautifulSoup

# Assuming current year
now = datetime.now()
filename = f"maerkte{now.year}.html"
filepath = os.path.join("..", "test", "data", filename)

# The event data was encoded differently before the pre PHP era
if now.year <= 2008:
    encoding = "ascii"
else:
    encoding = "utf_8_sig"

print(encoding)

with open(filepath, encoding=encoding, errors="ignore") as f:
    print(f.read())
