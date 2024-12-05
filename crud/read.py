from typing import Optional

from sqlalchemy import select

from db.bd_session import session
from func.converting_to_table import book_to_table
from model.book import Book, StatusBook


# Куча функций делает одно и тоже, надо пробрасывать параметр и его
# значение. Но пока что так.
def read_all() -> list[Book]:
    """Возвращает все книги из БД."""
    with session as s:
        books = s.execute(
            select(Book)
            .join(StatusBook)
        ).scalars().all()
    return books


def read_book(query_attr: str, value: str) -> Optional[Book]:
    """Возвращает книгу из БД по ключу и значению, если она существует.

    Доступные query_attr:
    id
    title
    """
    with session as s:
        book = s.execute(
            select(Book)
            .join(StatusBook)
            .where(getattr(Book, query_attr) == value)
        ).scalar()
    return book


def read_books(query_attr: str, value: str) -> list[Optional[Book]]:
    """Возвращает книги из БД по ключу и значению, если они есть.

    Доступные query_attr:
    author
    year
    status
    """
    with session as s:
        books = s.execute(
            select(Book)
            .join(StatusBook)
            .where(getattr(Book, query_attr) == value)
        ).scalars().all()
    return books


def show_status_all() -> list[StatusBook]:
    """Возвращает все статусы из БД"""
    with session as s:
        status = s.execute(
            select(StatusBook)
        ).scalars().all()
    return status


# !!!!!!!!!!!!!!!!!!!!!!!!
# Пока что не используются.
# !!!!!!!!!!!!!!!!!!!!!!!!
def show_status(status: str) -> StatusBook:
    """Возвращает статус из БД по названию"""
    with session as s:
        status = s.execute(
            select(StatusBook)
            .where(StatusBook.status == status)
        ).scalar()
    return status


def show_title_table(book_title: str) -> str:
    """Возвращает книгу по названию. Результат в виде таблицы."""
    book = read_book('title', book_title)
    return book_to_table(book)


def show_id_table(book_id: str) -> str:
    """Возвращает книгу по id. Результат в виде таблицы."""
    book = read_book('id', book_id)
    return book_to_table(book)
