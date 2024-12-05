from crud.read import (
    read_all,
    read_book,
    read_books,
)
from func.converting_to_table import data_to_table, book_to_table


def show_all_command() -> None:
    """Печатает все книги."""
    books = read_all()
    print(data_to_table(books))


def show_id_command(args: list[str]) -> None:
    """Печатает книгу, найденную по id если она есть."""
    if len(args) != 1:
        print('Должен быть 1 аргумент: book_id.')
        return

    book_id = args[0]
    book = read_book('id', book_id)
    print(book_to_table(book))


def show_title_command(args: list[str]) -> None:
    """Печатает книгу, найденную по названию, если она есть.

    Название может состоять из нескольких слов.
    """
    book_title = ' '.join(args)
    book = read_book('title', book_title)
    print(book_to_table(book))


def show_author_command(args: list[str]) -> None:
    """Печатаем книги, найденные по имени автора, если они есть.

    Функция копия show_title_command Надо прокидывать параметр и значение и
    сделать одну универсальную функцию, но пока так.
    """
    author = ' '.join(args)
    books = read_books('author', author)
    print(data_to_table(books))


def show_year_command(args: list[str]) -> None:
    """Печатает книги, найденные по указанному году, если они есть."""
    if len(args) != 1:
        print('Должен быть 1 аргумент: год.')
        return
    year = args[0]
    # это копия валидации из create_menu надо выносить в func.
    try:
        if 0 <= int(year) < 2025:
            books = read_books('year', year)
        else:
            raise ValueError
    except ValueError as e:
        print('Дата указывается числом: от 0 до 2024 год.')
        return

    print(data_to_table(books))


def show_menu():
    """Обработчик меню show."""
    running = True
    while running:
        print('-----------------------------------',
              'Меню просмотра книг, доступные команды:',
              '    "all" - Все книги.',
              '    "id 1" - Книга по id.',
              '    "title название" - Книга по названию.',
              '    "author автор" - Все книги автора.',
              '    "year год" - Все книги за указанный год.',
              '    "exit" - Вернуться.',
              sep='\n',
              )
        second_input = input('Введите команду: ')
        second_command = second_input.split()

        if second_command[0] == 'all':
            show_all_command()

        elif second_command[0] == 'exit':
            running = False

        elif second_command[0] == 'id':
            show_id_command(second_command[1:])

        elif second_command[0] == 'title':
            show_title_command(second_command[1:])

        elif second_command[0] == 'author':
            show_author_command(second_command[1:])

        elif second_command[0] == 'year':
            show_year_command(second_command[1:])

        else:
            print(f'{second_command} - такой команды нет')

        if running:
            input('"Enter" чтобы продолжить.')
