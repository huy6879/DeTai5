from flask import render_template, request, redirect
import dao
from app import app,login
from flask_login import login_user


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/user-login', methods=['post'])
def user_signin():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user)
    return render_template('login.html')

@app.route('/register', methods=['get','post'])
def user_register():
    return render_template('register.html')


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)