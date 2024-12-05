from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from model.book import Book, StatusBook

from db.bd_session import session
from func.converting_to_table import book_to_table


def create_book(title, author, year):
    """Создает новую книгу.

    Только название книги уникально, ожидаем только такую ошибку от базы.
    Если бд будет не доступна, то это я пока не учел (программа упадет).
    """
    new_book = Book(title=title, author=author, year=year)

    with session as s:
        status_in_stock = s.execute(
            select(StatusBook)
            .where(StatusBook.status == 'в наличии')
        ).scalar()
        new_book.status = status_in_stock.id
        s.add(new_book)
        try:
            s.commit()
            s.refresh(new_book)
            print('Книга ДОБАВЛЕНА.')
            return book_to_table(new_book)
        except IntegrityError:
            return f'ОШИБКА\nНазвание книги - "{title}" уже существует!'
