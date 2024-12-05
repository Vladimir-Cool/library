from sqlalchemy import select
from sqlalchemy.orm import Session

from model.book import Book, StatusBook
from db.bd_session import session


def add_data():
    """Функция для заполнения БД примерами"""
    status_in_stock = StatusBook(status='в наличии')
    status_issued = StatusBook(status='выдана')

    with session as s:
        s.add(status_in_stock)
        s.add(status_issued)
        s.commit()

    book_1 = Book(title='Идиот', author='Достоевский Ф.М.', year=1868)
    book_2 = Book(title='Преступление и наказание',
                  author='Достоевский Ф.М.',
                  year=1866)
    book_3 = Book(title='Бесы', author='Достоевский Ф.М.', year=1872)
    book_4 = Book(title='Братья Карамазовы',
                  author='Достоевский Ф.М.',
                  year=1880)

    with session as s:
        status_in_stock = s.execute(
            select(StatusBook)
            .where(StatusBook.status == 'в наличии')
        ).scalar()

        book_1.status = status_in_stock.id
        book_2.status = status_in_stock.id
        book_3.status = status_in_stock.id
        book_4.status = status_in_stock.id

        s.add(book_1)
        s.add(book_2)
        s.add(book_3)
        s.add(book_4)
        s.commit()


if __name__ == '__main__':
    add_data()
