from app import db
from app.models import User
import hashlib



def get_user_by_id(user_id):
    return User.query.get(user_id)



def add_user(fullname, date, address, username, password, phone, email):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(fullname=fullname.strip(), date= date, address=address.strip(),
                username=username.strip(), password=password, phone=phone.strip(), email=email.strip())
    db.session.add(user)
    db.session.commit()



def auth_user(username, password):
    if username and password:
        password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username),
                                 User.password.__eq__(password)).first()
