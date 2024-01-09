from app import db
from app.models import User, Flight
import hashlib

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_flight():
    return Flight.query.all()


def add_user(fullname, date, address, username, password, phone, cmnd, email):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(fullname=fullname.strip(), date= date, address=address.strip(),
                username=username.strip(), password=password, phone=phone.strip(), cmnd=cmnd.strip(), email=email.strip())
    db.session.add(user)
    db.session.commit()


def is_username_exists(username):
    existing_user = User.query.filter_by(username=username).first()
    return existing_user is not None

def is_cmnd_exists(cmnd):
    existing_cmnd = User.query.filter_by(cmnd=cmnd).first()
    return existing_cmnd is not None

def is_email_exists(email):
    existing_user = User.query.filter_by(email=email).first()
    return existing_user is not None


def is_phone_exists(phone):
    existing_user = User.query.filter_by(phone=phone).first()
    return existing_user is not None


def auth_user(username, password):
    if username and password:
        password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username),
                                 User.password.__eq__(password)).first()

def re_pass(id, new_password):
    user = db.session.query(User).filter_by(id=id).first()
    password_hash = str(hashlib.md5(new_password.strip().encode('utf-8')).hexdigest())
    user.password = password_hash
    db.session.commit()


def add_flight(departure, arrival, sanbaydi, sanbayden, ngaybay, gioibay, thoigianbay, ghehang1, ghehang2, sbtrunggian, thoigiandung,note, flightRoute_id):
    flight= Flight(departure=departure,
                   arrival=arrival,
                   sanbaydi=sanbaydi,
                   sanbayden=sanbayden,
                   ngaybay=ngaybay.strip(),
                   gioibay=gioibay.strip(),
                   thoigianbay=thoigianbay.strip(),
                   ghehang1=ghehang1.strip(),
                   ghehang2=ghehang2.strip(),
                   sbtrunggian=sbtrunggian.strip(),
                   thoigiandung=thoigiandung.strip(),
                   note=note.strip())
    db.session.add(flight)
    db.session.commit()
def get_flight(fr, to, date):
    # existing_departure = Flight.query.filter_by(departure=departure).first()
    # existing_arrival = Flight.query.filter_by(arrival=arrival).all()
    # existing_ngaybay = Flight.query.filter_by(ngaybay=ngaybay).first()
    # return existing_departure is not None
    flights = Flight.query.all()
    if fr and to and date:
        flights = [f for f in flights if
                   f.departure.lower().find(fr.lower()) >= 0 and f.arrival.lower().find(to.lower()) >= 0 and f.date == date]
    return flights

