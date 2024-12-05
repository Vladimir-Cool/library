"""Поле для тестов."""
from db import (
    create_table,
    delete_table,
    add_data,
    get_data
)
from crud.read import show_id_table, show_status_all, read_all, read_book
from crud.create import create_book
from crud.delete import delete_book
from func.converting_to_table import book_to_table, data_to_table


if __name__ == '__main__':
    # Так можно обновить БД.
    # delete_table()
    # create_table()
    # add_data()
    # get_data()

    print(data_to_table(read_all()))

    create_book('Книга10', 'Автор1', 2001)
    create_book('Книга11', 'Автор1', 2004)
    create_book('Книга12', 'Автор2', 2005)
    create_book('Книга10', 'Автор1', 2221)

    print(book_to_table(read_book('title', 'Книга10')))

    book_1 = read_book('title', 'Книга11')
    book_2 = read_book('title', 'Книга12')

    print(book_to_table(read_book('id', book_1.id)))
    print(book_to_table(read_book('id', book_2.id)))

    delete_book_1 = delete_book('title', 'Книга10')
    delete_book_2 = delete_book('id', book_1.id)
    delete_book_3 = delete_book('id', book_2.id)

    print(data_to_table([delete_book_1, delete_book_2, delete_book_3]))

