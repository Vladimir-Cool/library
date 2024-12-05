from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    """Базовый клас для моделей ORM.

    По его metadata будем создавать таблицы в БД.
    """

    id: Mapped[int] = mapped_column(primary_key=True)


class StatusBook(Base):
    """Класс статус книги."""

    __tablename__ = 'status_book'
    status: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.status})'


class Book(Base):
    """Класс книга.

    Надо отделить авторов как новый класс.
    """

    __tablename__ = 'book'
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    author: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(ForeignKey('status_book.id'))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.author}, {self.title})'

