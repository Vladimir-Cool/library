from typing import Optional

from sqlalchemy import delete

from crud.read import read_book
from db.bd_session import session
from model.book import Book


def delete_book(query_attr: str, value: str) -> Optional[Book]:
    """Удаление книги по указанному параметру.

    Если книга была удалена вернет ее.
    Если книги не было вернется None.

    Доступные query_attr:
    id
    title
    """
    book = read_book(query_attr, value)
    if book:
        with session as s:
            s.execute(
                delete(Book).where(getattr(Book, query_attr) == value)
            )
            s.commit()

        return book
