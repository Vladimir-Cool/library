from crud.update import update_status
from crud.read import show_status_all
from func.converting_to_table import book_to_table


# Константы тянут статусы из БД и затем показывают их пользователю для ввода.
STATUS = {s.status: s.id for s in show_status_all()}
STATUS_LIST = [f'"{status}" - {id}' for status, id in STATUS.items()]
STATUS_STR = '\n    '.join((STATUS_LIST))


def update_status_command(args: list[str]) -> None:
    """Команда изменения статуса книги."""
    if len(args) != 2:
        print('Должно быть 2 аргумента: book_id и status_id')
        return

    book_id, status_id = args
    if int(status_id) not in STATUS.values():
        print(f'Такого статуса нет! \nДоступные статусы:\n    {STATUS_STR}')
        return

    book = update_status(book_id, status_id)

    if book:
        print('Книга ИЗМЕНЕНА.',
              book_to_table(book),
              sep='\n')
    else:
        print(f'Книги с id = "{book_id}" нет.')


def update_menu():
    """Обработчик меню update."""
    running = True

    while running:
        print('-----------------------------------',
              'Меню изменения книг.',
              '    "status book_id status_id" - Изменить статус по id',
              '    "exit" - Вернуться.',
              'Доступные статусы:',
              f'    {STATUS_STR}',
              sep='\n',
              )
        second_input = input('Введите команду: ')
        second_command = second_input.split()

        if second_command[0] == 'status':
            update_status_command(second_command[1:])

        elif second_command[0] == 'title':
            running = False

        elif second_command[0] == 'exit':
            running = False

        if running:
            input('"Enter" чтобы продолжить.')
