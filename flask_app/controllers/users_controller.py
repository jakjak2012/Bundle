from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user_models import User


#home page
@app.route('/')
def index():
    return render_template('index.html')

#Login/registration page
@app.route('/sign_in')
def sign_in():
    return render_template('login.html')

#login in function that validates the user login info
@app.route('/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/sign_in')
    found_user = User.get_one_by_username(request.form)
    session["uid"] = found_user.id
    
    return redirect('/dashboard')

#logs out the user and redirects to the home page
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#resgister user function, validates user info and has password
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/sign_in')
    hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form
    }
    data['password'] = hash

    userid = User.create(data)
    session["uid"] = userid
    return redirect('/dashboard')

