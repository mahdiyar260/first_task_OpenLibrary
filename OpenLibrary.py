
import requests
import random
import csv
import os

def get_books(limit):
    
    url = "https://openlibrary.org/subjects/technology.json"
    params = {
        "limit": limit,
        "offset": random.randint(0, 500)
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    books = []

    for item in data.get("works", []):
        book = {
            "title": item.get("title"),
            "author": item.get("authors", [{}])[0].get("name") if item.get("authors") else None,
            "year": item.get("first_publish_year")
        }
        books.append(book)

    return books

def filter_books(books):
    result = []
    for book in books:
        try:
            if int(book["year"]) > 2000:
                result.append(book)
        except (TypeError, ValueError):
            continue

    return result

def save_books(books):

    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "books.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "author", "year"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for book in books:
            writer.writerow(book)

    print("CSV created.")

def main():
    books = filter_books(get_books(50))
    save_books(books)
    print("End.")

if __name__ == "__main__":
    main()