from datetime import datetime
from flask import render_template, g, request, flash, redirect, url_for
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user

from app import app, db, login_manager
from models import User

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        year = datetime.now().year,
    )

@app.route('/contact')
@login_required
def contact():
    return render_template(
        'contact.html',
        title = 'Contact',
        year = datetime.now().year,
        message = 'Your contact page.'
    )

@app.route('/about')
@login_required
def about():
    return render_template(
        'about.html',
        title = 'About',
        year = datetime.now().year,
        message = 'Your application description page.'
    )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html',
                               year = datetime.now().year)
    username = request.form.get('username')
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User(username=username, password=password, name=name, email=email)
    if user is not None:
        db.session.add(user)
        db.session.commit()
    flash('User added successfully')
    return redirect(url_for('home'), code=302)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html',
                               year = datetime.now().year)
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        flash('Invalid username or password')
        return render_template('login.html', 
                               year = datetime.now().year)
    flash('Login successful')
    login_user(user)
    return redirect(request.args.get('next') or url_for('home'))
 
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
