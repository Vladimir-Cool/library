from menu import (
    show_menu,
    create_menu,
    delete_menu,
    update_menu,
)


def main_menu():
    """Основное меню"""
    running = True
    while running:
        # Хорошо бы меню собирать автоматически =/
        print('-----------------------------------',
              'Доступные команды:',
              '    "create" - Создать новую книгу.',
              '    "show" - просмотреть книги.',
              '    "delete" - удалить книгу.',
              '    "update" - изменить книгу.',
              '    "exit" - выход.',
              sep='\n',
        )
        command = input('Введите команду: ').rstrip()

        if command == 'exit':
            running = False

        elif command == 'show':
            show_menu()

        elif command == 'create':
            create_menu()
            input('"Enter" чтобы продолжить.')

        elif command == 'delete':
            delete_menu()

        elif command == 'update':
            update_menu()

        else:
            print(f'{command} - нет такой команды')
