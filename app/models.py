from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum,Date
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
from datetime import datetime
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    address = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=False, unique=True)
    email = Column(String(30), nullable=False, unique=True)
    user_role = Column(Enum(UserRoleEnum), default= UserRoleEnum.USER)
    # def __str__(self):
    #     return self.name



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        import hashlib
        u1= User(fullname='Json Nguyen', date=datetime.strptime('26/11/2003', '%d/%m/%Y'), address='TPHCM', username='js',
                   password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()), phone='179', email='JS19@gmail.com', user_role=UserRoleEnum.USER)
        db.session.add(u1)
        db.session.commit()