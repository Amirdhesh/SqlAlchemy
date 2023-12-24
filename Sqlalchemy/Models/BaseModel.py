from sqlalchemy import Column, Integer, String, Sequence
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
engine = create_engine(os.getenv("mysqllink"), echo=True)


Base = declarative_base()


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    mail = Column(String(50), unique=True)


    def __init__ (self,Name,Mail):
        
        self.name = Name
        self.mail = Mail


Base.metadata.create_all(engine)
