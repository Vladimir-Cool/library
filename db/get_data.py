from sqlalchemy import select, Sequence, Row

from model.book import Book, StatusBook
from db.bd_session import session


def get_data():
    """Возвращает данные из таблиц для проверки"""
    with session as s:
        status = s.execute(
            select(StatusBook)
        ).all()
        print(status)

        status_in_stock = s.execute(
            select(StatusBook)
            .where(StatusBook.status == 'в наличии')

        ).scalar()
        print(type(status_in_stock))
        print(status_in_stock)

        books: Sequence[Row[tuple[Book]]] = s.execute(
            select(Book)
            .join(StatusBook)
        ).all()
        print(books)

        for el in books:
            print(el[0])


if __name__ == '__main__':
    get_data()

