# OpenLibrary Book Fetcher

A simple Python project for fetching books from the Open Library API, filtering them, and saving the results as a CSV file.

## Features

* Fetch a custom number of books
* Filter books by publication year
* Save results to CSV
* Simple and lightweight structure

## Installation

```bash
pip install requests
```

## Usage

```python
from functions import fetch_books, filter_books, save_to_csv

books = fetch_books(50)

filtered_books = filter_books(
    books,
    min_year=2000
)

save_to_csv(
    filtered_books,
    "books.csv"
)
```

## Project Structure

```text
project/
├── main.py
├── functions.py
└── README.md
```

## API

This project uses the Open Library Search API:

```text
https://openlibrary.org/search.json
```

## Output

The generated CSV file contains:

* Title
* Author
* Publication Year
* ISBN
