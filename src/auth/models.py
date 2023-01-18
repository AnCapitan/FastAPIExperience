from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData

from database import Base


class User(Base):
    __tablename__ = 'User'

    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    avatar = Column('avatar', String)
    #hashed_password = Column("hashed_password", String, nullable=False)
    #is_active = Column("is_active", Boolean, default=True, nullable=False)
    #is_superuser = Column("is_superuser", Boolean, default=False, nullable=False)
    #is_verified = Column("is_verified", Boolean, default=False, nullable=False)
