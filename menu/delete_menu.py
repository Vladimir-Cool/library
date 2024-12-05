from crud.delete import delete_book
from func.converting_to_table import book_to_table


def delete_id_command(args: list[str]) -> None:
    """Команда удаления книги по id"""
    if len(args) != 1:
        print('Аргумент должен быть один: book_id')
        return

    book_id = args[0]
    book = delete_book('id', book_id)

    if book:
        print('Книга УДАЛЕНА.',
              book_to_table(book),
              sep='\n')
    else:
        print(f'Книги с id = "{book_id}" нет.')


def delete_title_command(args: list[str]) -> None:
    """Команда удаления книги по названию

    Функция очень похожа на delete_id_command да.
    Мешать функции и делать условие пока не хочу, как сделать лучше пока не
    придумал. Но править надо!
    """
    book_title = ' '.join(args)
    book = delete_book('title', book_title)

    if book:
        print('Книга УДАЛЕНА.',
              book_to_table(book),
              sep='\n')
    else:
        print(f'Книги с Названием = "{book_title}" нет.')


def delete_menu():
    """Обработчик меню delete"""
    running = True
    is_exit = False
    while running:
        # Хорошо бы меню собирать автоматически =/
        print('-----------------------------------',
              'Меню удаления книг.',
              '    "id" - Удалить по id',
              '    "title" - Удалить по названию',
              '    "exit" - Вернуться.',
              sep='\n',
              )
        second_input = input('Введите команду: ')
        second_command = second_input.split()

        if second_command[0] == 'id':
            delete_id_command(second_command[1:])
            running = False

        elif second_command[0] == 'title':
            delete_title_command(second_command[1:])
            running = False

        elif second_command[0] == 'exit':
            running = False
            is_exit = True

        else:
            print(f'Нет команды - {second_command[0]}')
        # Это нужно чтобы сразу выйти из контекста удаления.
        # Предполагается что удаление серьезный шаг, и будь это ошибка
        # или успех, пользователь выходит из этого контекста автоматически.
        if not is_exit:
            input('"Enter" чтобы продолжить.')
