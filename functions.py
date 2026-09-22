
import requests
import csv


def fetch_books(limit=20):

    """
    Sending a request to Open Library and receiving a list of books.
    """

    url = "https://openlibrary.org/search.json"
    params = {
        "q": "book",
        "limit": limit
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    books = []

    for item in data.get("docs", []):

        title = item.get("title", "")
        authors = ", ".join(item.get("author_name", []))
        year = item.get("first_publish_year", "")
        isbns = item.get("isbn", [""])[0] if item.get("isbn") else ""

        books.append({
            "title": title,
            "author": authors,
            "year": year,
            "isbn": isbns
        })

    return books


def filter_books(books, min_year=None, max_year=None):

    """
    Filtering books based on publication year.
    """

    filtered_books = []

    for book in books:

        year = book.get("year", "")

        if not year:
            continue

        if min_year and year < min_year:
            continue

        if max_year and year > max_year:
            continue

        filtered_books.append(book)

    return filtered_books


def save_to_csv(books, filename="books.csv"):

    """
    Save the book list as a CSV file.
    """

    if not books:
        print("There is no data to save.")
        return

    fieldnames = ["title", "author", "year", "isbn"]

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(books)

    print(f"{len(books)} books were successfully saved to the file '{filename}'.")


if __name__ == "__main__":

    # Retrieve books without filters
    books_data = fetch_books(limit=100)

    # Filter books published after 2000
    filtered_books = filter_books(
        books_data,
        min_year=2001
    )

    # Save in CSV file
    save_to_csv(
        filtered_books,
        filename="books_after_2000.csv"
    )