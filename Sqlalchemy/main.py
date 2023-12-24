from Models.BaseModel import engine
from Models.BaseModel import Students
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()
s1 = Students("Amirdhesh","amirdhesh123@gmail.com")
session.add(s1)
session.commit()