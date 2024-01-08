import time
from flask import render_template, request, redirect, session
import dao
from app import db
from app import app,login
from flask_login import login_user, logout_user, current_user, UserMixin
from app.models import User, Flight, Airport

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user-login", methods=['get','post'])
def user_signin():
    err_msg = ''
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            role = current_user.user_role.value
            if role == 3:
                return redirect('/admin')
            else:
                return redirect('/')
        else:
            err_msg = 'Username hoac Password KHONG chinh xac !!!'

    return render_template('login.html', err_msg=err_msg)



@app.route('/register', methods=['get','post'])
def user_register():
    err_msg = ''
    if request.method.__eq__('POST'):
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        address = request.form.get('address')
        password = request.form.get('password')
        phone = request.form.get('phone')
        date = request.form.get('date')
        cmnd = request.form.get('cmnd')
        email = request.form.get('email')
        confirm = request.form.get('confirm')
        try:
            if dao.is_username_exists(username):
                raise Exception('Tên đăng nhập đã tồn tại!')
            elif len(password) < 8:
                raise Exception('Mật khẩu phải có ít nhất 8 ký tự!')
            elif dao.is_phone_exists(phone):
                raise Exception('Số điện thoại đã tồn tại')
            elif dao.is_cmnd_exists(cmnd):
                raise Exception('Số căn cước đã tồn tại')
            elif dao.is_email_exists(email):
                raise Exception('Email đã tồn tại')
            elif password.strip().__eq__(confirm.strip()):
                dao.add_user(fullname=fullname, date=date,address=address, username=username,
                             password=password, phone=phone, cmnd=cmnd, email=email)
                return redirect('/user-login')
            else:
                err_msg = 'Mật khẩu không trùng khớp!'
        except Exception as ex:
            err_msg = 'He thong dang co loi : ' + str(ex)

    return render_template('register.html',err_msg=err_msg)




@app.route('/user-logout')
def user_logout():
    logout_user()
    return redirect("/")

@app.route('/user-info/account/repassword/<int:user_id>', methods=['get','post'])
def user_repass(user_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    err_msg = ''
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        new_password = request.form.get('new_password')
        confirm = request.form.get('confirm')
        import hashlib
        password1 = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        try:
            if password1 == user.password and len(new_password) < 8:
                raise Exception('Mật khẩu phải có ít nhất 8 ký tự!')
            elif password1 == user.password and new_password.strip().__eq__(confirm.strip()):
                dao.re_pass(id=user_id,new_password=new_password)
                err_msg = 'Cập nhật thanh công'
                user_logout()
                return redirect('/user-login')
            else:
                err_msg = 'Mật khẩu không trùng khớp!'
        except Exception as ex:
                err_msg = 'Hệ thống đang có lỗi : ' + str(ex)

    return render_template('re_password.html', user=user, err_msg=err_msg)



@app.route('/user-info/account/<int:user_id>')
def user_info(user_id):
    user = User.query.get(user_id)
    return render_template('user_info.html', user=user)



@app.route('/user-info/personal/<int:user_id>')
def personal_info(user_id):
    user = User.query.get(user_id)
    return render_template('personal_info.html', user=user)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/add_flights', methods=['get','post'])
def add_flights():
    airports = Airport.query.all()
    flights = Flight.query.all()
    err_msg = ''
    if request.method.__eq__('POST'):
        sanbaydi = request.form.get('airport1')
        sanbayden = request.form.get('airport2')
        ngaybay = request.form.get('date1')
        gioibay = request.form.get('time1')
        thoigianbay = request.form.get('time2')
        ghehang1 = request.form.get('1stclass')
        ghehang2 = request.form.get('2ndclass')
        sbtrunggian = request.form.get('AP_TG1')
        thoigiandung = request.form.get('pendingT')
        note = request.form.get('note')

        dao.add_flight(sanbaydi=sanbaydi,sanbayden=sanbayden,ngaybay=ngaybay,gioibay=gioibay,thoigianbay=thoigianbay,
                       ghehang1=ghehang1,ghehang2=ghehang2,sbtrunggian=sbtrunggian,thoigiandung=thoigiandung,note=note)
        err_msg = 'Thêm thành công'
    else:
        err_msg = 'Thêm không thành công'

    return render_template('add_flights.html', airports=airports,flights=flights, err_msg=err_msg)

@app.route("/flight_list")
def search_flight():

    fr = request.args.get("departure")
    to = request.args.get("arrival")
    flight = dao.get_flight(fr=fr, to=to)
    # session['From'] = fr
    # session['To'] = to
    return render_template('flight_list.html', flight=flight, fr=fr, to=to)

# @app.route("/flight_list" , methods=['post'])
# def flight_list():
#     return render_template('flight_list.html')

# @app.route("/test.html")
# def test():
#     return render_template('test.html')
if __name__ == '__main__':
    from app import admin
    app.run(debug=True)