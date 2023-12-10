from flask import render_template, request, redirect
import dao
from app import app,login
from flask_login import login_user, logout_user
from app.models import User



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
        email = request.form.get('email')
        confirm = request.form.get('confirm')
        try:
            if password.strip().__eq__(confirm.strip()):
                dao.add_user(fullname=fullname, date=date,address=address, username=username,
                             password=password, phone=phone, email=email)
                return redirect('/user-login')
            else:
                err_msg = 'Mat Khau KHONG Khop !!!'
        except Exception as ex:
            err_msg = 'He thong dang co loi : ' + str(ex)

    return render_template('register.html',err_msg=err_msg)

@app.route('/user-logout')
def user_logout():
    logout_user()
    return redirect("/")

@app.route('/user-info/<int:user_id>')
def user_info(user_id):
    user = User.query.get(user_id)

    return render_template('user_info.html', user=user)

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)