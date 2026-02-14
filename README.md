# OpenLibrary Books Fetcher

This Python script fetches 50 books from the **OpenLibrary API**, filters only the books published **after the year 2000**, and saves the result in a CSV file.

## Features
- Fetch books from the OpenLibrary public API.
- Filter books by publication year (>2000).
- Save the output in a CSV file (`books.csv`) with columns: `title`, `author`, `year`.
- Randomized selection to get different books each time the script runs.

## Requirements
- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
