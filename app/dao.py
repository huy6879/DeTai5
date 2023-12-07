
from app.models import User
import hashlib



def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = password or ""
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()
