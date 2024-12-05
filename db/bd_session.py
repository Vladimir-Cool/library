from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine(f'sqlite+pysqlite:///db/library.db', echo=False)
session = Session(engine, expire_on_commit=True)
