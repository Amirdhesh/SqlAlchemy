from Models.BaseModel import engine
from Models.BaseModel import Students
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def Add_single_student():
    s1 = Students("Amirdhesh", "amirdhesh123@gmail.com")
    session.add(s1)
    session.commit()


def Add_multiple_student():
    session.add_all(
        [
            Students("Dharaneesh", "Dharanessh@gmail.com"),
            Students("Naveen", "Naveen@gmail.com"),
            Students("Thilak", "Thilak@gmail.com"),
            Students("Abinesh", "Abinesh@gmail.com"),
        ]
    )
    session.commit()


def Return_all_values():
    result = session.query(Students).all()
    for i in result:
        print(f"Name : {i.name} , Mail : {i.mail}")


def Updata_name():
    session.query(Students).filter(Students.name == "Thilak").update(
        {Students.name: "Mridul"}, synchronize_session="fetch"
    )
    session.commit()
