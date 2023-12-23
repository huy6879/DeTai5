from app.models import User, UserRoleEnum, Schedules
from app import app,db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect


admin = Admin(app=app, name="OU AIRLINE Administration", template_mode='bootstrap4')

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/user-login')

class SchedulesView(ModelView):
    can_view_details = True



admin.add_view(ModelView(User, db.session))
admin.add_view(LogoutView(name='Đăng xuất'))
admin.add_view(SchedulesView(Schedules,db.session))
# admin.add_view(ModelView(name=''))