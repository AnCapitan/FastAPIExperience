from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey
import datetime

from database import Base


class Item(Base):
    __tablename__ = 'Item'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String, nullable=False)
    description = Column('description', String, nullable=False)
    create_at = Column("create_at", TIMESTAMP, default=datetime.datetime.now)
