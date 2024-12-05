from crud.create import create_book


def get_valid_str(
        placeholder: str = 'Введите :',
        lenght: int = 300,
) -> str:
    """Валидация ввода строки"""
    title_input = input(placeholder)
    if title_input == 'exit':
        return title_input

    if len(title_input) < lenght:
        return title_input


def get_valid_year(placeholder: str = 'Введите год создания:') -> str:
    """Валидация ввода года"""
    running = True
    while running:
        year_input = input(placeholder)
        if year_input == 'exit':
            return year_input

        try:
            if 0 < int(year_input) < 2025:
                return year_input
        except ValueError as e:
            pass

        print('Дата введена не правильно, дата указывается числом '
              'от 0 до 2024 года')


def create_menu():
    """Обработчик меню create"""
    running = True
    while running:
        print('-----------------------------------',
              'Меню добавления новой книги.',
              'Нужно будет ввести название книги, автора и год создания.',
              '"exit" - Вернуться.',
              sep='\n',
              )

        title = get_valid_str('Введите название книги: ')
        if title == 'exit':
            running = False
            continue

        author = get_valid_str('Введите автора: ')
        if author == 'exit':
            running = False
            continue

        year = get_valid_year()
        if year == 'exit':
            running = False
            continue

        print(create_book(title, author, year))

        running = False
