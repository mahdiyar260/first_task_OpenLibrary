
from functions import fetch_books, filter_books, save_to_csv

try:

    books = fetch_books(50)
    filtered_books = filter_books(books, min_year=2000)
    save_to_csv(filtered_books)

except Exception as e:
    print(f"Error: \n{e}")
