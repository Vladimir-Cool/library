from typing import Optional

from tabulate import tabulate

from model.book import Book


def data_to_table(raw_data: list[Book]) -> str:
    """Преобразуем список книг к табличному выводу."""
    headers = ['id', 'author', 'title', 'year', 'status']
    data = [[book.id, book.author, book.title, book.year,
             book.status] for
            book in raw_data]

    return tabulate(data, headers=headers, tablefmt='psql')


def book_to_table(raw_book: Optional[Book]):
    """Преобразуем одну книгу к табличному выводу."""
    headers = ['id', 'author', 'title', 'year', 'status']
    if raw_book:
        data = [[raw_book.id,
                raw_book.author,
                raw_book.title,
                raw_book.year,
                raw_book.status,
        ]]
    else:
        data = []

    return tabulate(data, headers=headers, tablefmt='psql')
