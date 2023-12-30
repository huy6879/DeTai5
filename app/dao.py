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

def add_flight(sanbaydi, sanbayden, ngaybay, gioibay, thoigianbay, ghehang1, ghehang2, sbtrunggian, thoigiandung,note):
    flight= Flight(sanbaydi=sanbaydi,
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
def get_flight(cate_id=None, fr=None, to=None):
    flights = Flight.query.all()

    if cate_id:
        flights = [f for f in flights if f.flight_type.id == int(cate_id)]

    if fr and to:
        flights = [f for f in flights if
                   f.departure_point.lower().find(fr.lower()) >= 0 and f.destination.lower().find(to.lower()) >= 0]
    elif fr:
        flights = [f for f in flights if f.departure_point.lower().find(fr.lower()) >= 0]
    elif to:
        flights = [f for f in flights if f.destination.lower().find(to.lower()) >= 0]

    return flights