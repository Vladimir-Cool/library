"""Работа с БД"""

from db.add_data import add_data
from db.create_table import create_table, delete_table
from db.get_data import get_data

__all__ = [
    create_table,
    delete_table,
    add_data,
    get_data,
]