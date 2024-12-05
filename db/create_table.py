from sqlalchemy.orm import Session

from db.bd_session import engine, session
from model.book import Base


def create_table():
    """Создаем таблицы в бд

    Лучше использовать Alembic для миграций БД,
    но времени на задание не много.
    """
    with session.begin():
        Base.metadata.create_all(engine)


def delete_table():
    """Удаление таблиц в БД

    Лучше использовать Alembic для миграций БД,
    но времени на задание не много.
    """
    with session.begin():
        Base.metadata.drop_all(engine)


if __name__ == '__main__':

    with Session(engine) as session:
        delete_table()
        create_table()
