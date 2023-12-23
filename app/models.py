from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, Date
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


class Schedules(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    sanbaydi = Column(String(50), nullable=False)
    sanbayden = Column(String(50), nullable=False)
    ngaybay = Column(Date, nullable=False)
    gioibay = Column(String(10), nullable=False)
    thoigianbay = Column(String(10), nullable=False)
    ghehang1 = Column(String(5), nullable=False, unique=True)
    ghehang2 = Column(String(5), nullable=False, unique=True)
    sbtrunggian = Column(String(50), nullable=False)
    thoigiandung = Column(String(10), nullable=False)
    note = Column(String(100), nullable=False)

    # # ngaybay = Column(Date, nullable=False)
    # # ngaybay = Column(String(100), nullable=False)
    # # gioibay = Column(String(50), nullable=False, unique=True)
    # # thoigianbay = Column(String(50), nullable=False)
    # # ghehang1 = Column(String(15), nullable=False, unique=True)
    # # ghehang2 = Column(String(30), nullable=False, unique=True)
    # # sbtrunggian = Column(String(15), nullable=False, unique=True)
    # # thoigiandung = Column(String(30), nullable=False, unique=True)
    # note = Column(String(100), nullable= False, unique= True)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # import hashlib
        # u1= User(fullname='Nguyễn Gia Huy', date=datetime.strptime('26/11/2003', '%d/%m/%Y'), address='141/17/16 Đường số 11 Phường bình hưng hòa quận Bình Tân', username='huybambo',
        #            password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()), phone='0983325261', email='giahuy261103@gmail.com', cmnd='2135133154', user_role=UserRoleEnum.ADMIN)

        # u2= User(fullname='Phạm Tiến Dũng', date=datetime.strptime('19/03/2003', '%d/%m/%Y'), address='Nhà Bè', username='dungpham1903',
        #            password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()), phone='0945540161', email='ptd.zuxg193@gmail.com', cmnd='2154050055', user_role=UserRoleEnum.ADMIN)
        # db.session.add(u2)
        # db.session.add(u1)
        c1 = Schedules(sanbaydi='Tan Son Nhat', sanbayden='Noi Bai', ngaybay=datetime.strptime('21/12/2023', '%d/%m/%Y'),
                       gioibay='15:00PM', thoigianbay='2', ghehang1='60', ghehang2='60', sbtrunggian='khong co', thoigiandung='khong co', note='0')

        db.session.add(c1)
        db.session.commit()
