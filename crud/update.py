from typing import Optional

from sqlalchemy import update

from crud.read import read_book
from db.bd_session import session
from model.book import Book


def update_status(book_id: str, status_id: str) -> Optional[Book]:
    """Изменяет статус книги.

    Тут я в начале получаю объект, который собираюсь изменить, для того
    чтобы проверить есть он или нет. Лучше делать это за 1 запрос в бд и
    анализировать вывод, надо это проработать.
    """
    book = read_book('id', book_id)
    if book:
        with session as s:
            s.add(book)
            s.execute(
                update(Book)
                .where(Book.id == book_id)
                .values(status=status_id)
            )
            s.commit()
            s.refresh(book)
        return book
