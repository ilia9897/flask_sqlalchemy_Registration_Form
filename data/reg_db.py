from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy import Column
from data.db_session import SqlAlchemyBase

class Reg_form(SqlAlchemyBase):
    __tablename__ = 'reg'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    address = Column(String, nullable=True)
