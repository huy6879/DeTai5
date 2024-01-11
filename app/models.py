
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
    tickets = relationship('Ticket', backref='user', lazy=True)

    # def __str__(self):
    #     return self.name




class Flight(db.Model):
        __tablename__ = 'flight'
    
        id = Column(Integer, primary_key=True, autoincrement=True)
        D_air = Column(String(100), nullable=False)
        A_air = Column(String(100), nullable=False)
        # Date = Column(Date, nullable=False)
        T_time = Column(DateTime, nullable=False)
        E_time = Column(DateTime, nullable=False)
        T1_quantity = Column(String(10), nullable=False)
        T2_quantity = Column(String(10), nullable=False)
        I_air = Column(String(100), nullable=False)
        I2_air = Column(String(100), nullable=True)
        S_time = Column(String(20), nullable=False)
        S2_time = Column(String(20), nullable=True)
        Flight_time = Column(String(20), nullable=False)
        note = Column(String(50), nullable=False)
        flightRoute_id = Column(Integer, ForeignKey('flightroute.id'), nullable=False)
        tickets = relationship('Ticket', backref='flight', lazy=True)


class FlightRoute(db.Model):
    __tablename__ = 'flightroute'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    flights = relationship('Flight', backref='flightroute', lazy=True)
    receipt_details = relationship('ReceiptDetail', backref='flightroute', lazy=True)


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now())





class Ticket(BaseModel):
    __tablename__ = 'ticket'

    flight_name = Column(String(50),nullable=False)
    passenger_name = Column(String(50), nullable=False)
    cmnd = Column(String(30), nullable=False)
    phone = Column(String(15), nullable=False)
    type = Column(String(10), nullable=False)
    price = Column(Float, default=0)
    flight_id = Column(Integer, ForeignKey(Flight.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=True)
    receipt_details = relationship('ReceiptDetail', backref='ticket', lazy=True)



# class Receipt(BaseModel):
#     user_id = Column(Integer, ForeignKey(User.id), nullable=True)
#     details = relationship('ReceiptDetail', backref='receipt', lazy=True)


class ReceiptDetail(BaseModel):
    flightRoute_id = Column(Integer, ForeignKey(FlightRoute.id), nullable=False)
    ticket_id = Column(Integer, ForeignKey(Ticket.id), nullable=False)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0)




    # departure = Column(String(50), nullable=False)
    # arrival = Column(String(50), nullable=False)
    # ngaybay = Column(Date, nullable=False)
    # giobay = Column(DateTime, nullable=False)
    # gioden = Column(DateTime, nullable=False)
    # thoigianbay = Column(String(5), nullable=False)
    # ghehang1 = Column(String(5), nullable=False)
    # ghehang2 = Column(String(5), nullable=False)
    # sbtrunggian1 = Column(String(50), nullable=True)
    # sbtrunggian2 = Column(String(50), nullable=True)
    # thoigiandung = Column(String(10), nullable=True)
    # note = Column(String(100))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # ap1= Airport(name='Tan Son Nhat', city='HCM')
        # ap2= Airport(name='Noi Bai', city='HN')
        # ap3= Airport(name='Da Nang', city='Da Nang')
        # db.session.add(ap1)
        # db.session.add(ap2)
        # db.session.add(ap3)
        # db.session.commit()
        # u1= User(fullname='Nguyễn Gia Huy', date=datetime.strptime('26/11/2003', '%d/%m/%Y'), address='141/17/16 Đường số 11 Phường bình hưng hòa quận Bình Tân', username='huybambo',
        #            password   =str(hashlib.md5('123'.encode('utf-8')).hexdigest()), phone='0983325261', email='giahuy261103@gmail.com', cmnd='2135133154', user_role=UserRoleEnum.ADMIN)

        # u2= User(fullname='Phạm Tiến Dũng', date=datetime.strptime('19/03/2003', '%d/%m/%Y'), address='Nhà Bè', username='dungpham1903',
        #            password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()), phone='0945540161', email='ptd.zuxg193@gmail.com', cmnd='2154050055', user_role=UserRoleEnum.ADMIN)
        # db.session.add(u2)
        # db.session.add(u1)

        # c1 = Schedules(sanbaydi='Tan Son Nhat', sanbayden='Noi Bai', ngaybay=datetime.strptime('21/12/2023', '%d/%m/%Y'),
        #                gioibay='15:00PM', thoigianbay='2', ghehang1='60', ghehang2='60', sbtrunggian='khong co', thoigiandung='khong co', note='0')
        #
        # db.session.add(c1)
        # db.session.commit()

#         db.create_all()
#         # import hashlib
#         # u1 = User(fullname='Nguyễn Gia Huy', date=datetime.strptime('26/11/2003', '%d/%m/%Y'), address='141/17/16 Đường số 11 Phường bình hưng hòa quận Bình Tân', username='huybambo',
#         #            password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()), phone='0983325261', email='giahuy261103@gmail.com', cmnd='2135133154', user_role=UserRoleEnum.ADMIN)
#         #
#         # db.session.add(u1)
#         # db.session.commit()
#         import hashlib
#         u3= User(fullname='Nhanvien', date=datetime.strptime('19/03/2003', '%d/%m/%Y'), address='Nhà Bè', username='nhanvien1',
#                     password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()), phone='232323', email='nv1@gmail.com', cmnd='232323', user_role=UserRoleEnum.EMPLOYEE)
#         db.session.add(u3)
#         db.session.commit()
# <<<<<<< HEAD
#         c2 = Flight(sanbaydi='Tan Son Nhat', sanbayden='Da Nang', ngaybay=datetime.strptime('21/12/2023', '%d/%m/%Y'),
#                     gioibay='15:00PM', thoigianbay='2', ghehang1='88', ghehang2='80', sbtrunggian='Hue', thoigiandung='50', note='0')
#
#         db.session.add(c2)
#         db.session.commit()
#         Date = datetime.strptime('09/01/2024', '%d/%m/%Y')
#         f4 = Flight(D_air='Tan Son Nhat',
#                     A_air='Ha Noi',
#                     T_time= datetime.strptime('10:00', '%H:%M'),
#                     E_time= datetime.strptime('12:00','%H:%M'),
#                     T1_quantity='90', T2_quantity='120', I_air='Lam Dong', I2_air='Phu Yen', S_time='130', S2_time='60', Flight_time='60', note='1', flightRoute_id='2')
#
#
        # t1 = Ticket(flight_name='TSN - DAD', passenger_name='Van Tien', cmnd='12389', phone='124790',
        #                  type='1', price=2000000, flight_id='1', user_id='5')
        # db.session.add(f4)
        # db.session.commit()
# =======
#             c1 = Flight(departure='Ho Chi Minh', arrival='Ha Noi', sanbaydi='Tan Son Nhat', sanbayden='Noi Bai', ngaybay=datetime.strptime('21/12/2023', '%d/%m/%Y'),
#                         gioibay='15:00PM', thoigianbay='2', ghehang1='88', ghehang2='80', sbtrunggian='đsdsa', thoigiandung='kcohong ', note='0')
#

#             db.session.add(c1)
#             db.session.commit()
#         c4 = Flight(departure='HaNoi', arrival='HoChiMinh',
#                     ngaybay=datetime.strptime('8/1/2024', '%d/%m/%Y'),
#                     giobay=datetime.strptime('10:00', '%H:%M'),
#                     gioden=datetime.strptime('12:00','%H:%M'),
#                     thoigianbay='2', ghehang1='88', ghehang2='80', sbtrunggian1='Không có',sbtrunggian2='Không có',
#                     thoigiandung='0', note='0')
#         db.session.add(c4)
#         db.session.commit()
#         route = Flight_route(departure='Ho Chi Minh', arrival='Da Nang')
#         db.session.add(route)
#         db.session.commit()

