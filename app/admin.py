from app.models import User, UserRoleEnum, Airport, Flight
import dao
from app import app,db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect, request, render_template

admin = Admin(app=app, name="OU AIRLINE Administration", template_mode='bootstrap4')

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyUserView(AuthenticatedAdmin):
    column_list = ['id', 'fullname', 'date', 'phone','cmnd','email', 'user_role']
    column_searchable_list = ['fullname']


class MyAirPortView(AuthenticatedAdmin):
    column_list = ['id','name','city']
    column_searchable_list = ['city']



class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/user-login')


class FlightView(AuthenticatedUser):
    @expose("/")
    def index(self):
        flight = dao.get_flight()
        return self.render('/admin/flight_management.html', Flight=flight)



admin.add_view(MyUserView(User, db.session))
admin.add_view(FlightView(name='Chuyến bay'))
admin.add_view(MyAirPortView(Airport, db.session))
admin.add_view(LogoutView(name='Đăng xuất'))
