from sqlalchemy import Column, Integer, String, Float , Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    sdt = Column(String(15), nullable=False, unique=True)
    email = Column(String(30), nullable=False, unique=True)
    user_role = Column(Enum(UserRoleEnum), default= UserRoleEnum.USER)
    def __str__(self):
        return self.name



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        import hashlib
        u2 = User(name='nvA1', username = 'admin3',
                 password = str(hashlib.md5('123'.encode('utf-8')).hexdigest()),sdt = '15245', email='nv333@gmail.com', user_role=UserRoleEnum.USER)
        db.session.add(u2)
        db.session.commit()