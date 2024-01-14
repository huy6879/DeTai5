from app.models import User, UserRoleEnum, Flight, FlightRoute, Regulations
from app import app,db, dao, utils
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose, AdminIndexView
from flask_login import logout_user, current_user
from flask import redirect, request, render_template
from datetime import datetime



class MyAdmin(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html', stats=utils.count_flight_by_route())



admin = Admin(app=app,name="OU AIRLINE Administration", template_mode='bootstrap4',  index_view=MyAdmin())

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyUserView(AuthenticatedAdmin):
    column_list = ['id', 'fullname', 'date', 'phone','cmnd','email', 'user_role']
    column_searchable_list = ['fullname']


class MyFlightRouteView(AuthenticatedAdmin):
    column_list = ['id','name']
    column_searchable_list = ['name']


class MyRyRegulations(AuthenticatedAdmin):
    column_list = ['id', 'flight_mTime', 'sl_TGA', 'time_mS', 'time_MAS', 'time_G', 'time_E']


class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/user-login')


class FlightView(AuthenticatedUser):
    @expose("/")
    def index(self):
        Routes = FlightRoute.query.all()
        flight = dao.get_flight()
        return self.render('/admin/flight_management.html', Flight=flight, Routes=Routes)

class StatsView(AuthenticatedUser):
    @expose('/')
    def index(self):
        month = request.args.get('month')
        year = request.args.get('year')
        if year or month:
            month = month
            year = year
        else:
            month = None
            year = 2024
        return self.render('/admin/stats.html',stats=utils.stats_revenue(month=month), year_stats=utils.stats_revenue_by_year(year=year))


admin.add_view(MyUserView(User, db.session))
admin.add_view(FlightView(name='Flight'))
admin.add_view(MyFlightRouteView(FlightRoute, db.session))
admin.add_view(MyRyRegulations(Regulations,db.session))
admin.add_view(StatsView(name='Stats'))
admin.add_view(LogoutView(name='Logout'))
