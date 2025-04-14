from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy import Column
from data.db_session import SqlAlchemyBase

class Reg_form(SqlAlchemyBase):
    __tablename__ = 'reg'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    position = Column(String)
    speciality = Column(String)
    address = Column(String)
