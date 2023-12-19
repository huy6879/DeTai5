from app import app
from flask_admin import Admin

admin = Admin(app=app, name="E-commerce Administration", template_mode='bootstrap4')