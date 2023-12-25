from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum,Date, DateTime
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
from datetime import datetime
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    EMPLOYEE = 2
    ADMIN = 3


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    address = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=False, unique=True)
    cmnd = Column(String(30), nullable=False, unique=True)
    email = Column(String(30), nullable=False, unique=True)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    # def __str__(self):
    #     return self.name

class Airport(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False, unique=True)
    def __str__(self):
        return self.name

class Flight(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    D_air = Column(String(100), nullable=False)
    A_air = Column(String(100), nullable=False)
    T_time = Column(DateTime, nullable=False)
    A_time = Column(DateTime, nullable=False)
    T1_quantity = Column(String(10), nullable=False)
    T2_quantity = Column(String(10), nullable=False)
    I_air = Column(String(100), nullable=True)
    S_time = Column(String(20), nullable=True)
    note = Column(String(50), nullable=False)





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # import hashlib
        # u1 = User(fullname='Nguyễn Gia Huy', date=datetime.strptime('26/11/2003', '%d/%m/%Y'), address='141/17/16 Đường số 11 Phường bình hưng hòa quận Bình Tân', username='huybambo',
        #            password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()), phone='0983325261', email='giahuy261103@gmail.com', cmnd='2135133154', user_role=UserRoleEnum.ADMIN)
        #
        # db.session.add(u1)
        # db.session.commit()
        f2 = Flight(D_air='Tan Son Nhat', A_air='Phu Quoc ', T_time='12:03 AM', A_time='9:05 PM',
                    T1_quantity='20', T2_quantity='30',I_air='Liên Khương', S_time ='30 Phút', note='0')
        db.session.add(f2)
        db.session.commit()