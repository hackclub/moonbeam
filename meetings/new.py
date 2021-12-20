# This file is meant to create a new meeting note file automatically.

from datetime import datetime
import os

now = datetime.now()
ordinal = (
    "th" if 11 <= now.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(now.day % 10, "th")
)

folder = now.strftime("%Y - %B").lower()
file = os.path.join(folder, f"{str(now.day)}{ordinal}.md")
template = now.strftime(
    f"""# %-d{ordinal} of %B

Recording of meeting: []()

## tl;dr

-

## Hardware

-

## Software

-

## Communications

-

## Other

-
"""
)


if not os.path.isdir(folder):
    os.makedirs(folder)

with open(file, "w") as note_file:
    note_file.write(template)
print(f'Created "{file}" open it with your favorite editor')
