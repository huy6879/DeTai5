from app import db
from app.models import User
import hashlib



def get_user_by_id(user_id):
    return User.query.get(user_id)



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
