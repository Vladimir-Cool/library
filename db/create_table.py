from db.bd_session import engine
from model.book import Base


def create_table():
    """Создаем таблицы в бд

    Лучше использовать Alembic для миграций БД,
    но времени на задание не много.
    """
    Base.metadata.create_all(engine)


def delete_table():
    """Удаление таблиц в БД

    Лучше использовать Alembic для миграций БД,
    но времени на задание не много.
    """
    Base.metadata.drop_all(engine)


if __name__ == '__main__':

    delete_table()
    create_table()
