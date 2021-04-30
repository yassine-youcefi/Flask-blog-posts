from flask import render_template, url_for, flash, redirect
from app.forms import Sign_up, Login
from app.models import User, Post
from app import application, db, bcrypt
from flask_login import login_user

posts = [

    {
        'author': 'yassine youcefi',
        'title': 'Blog jdid hada 1',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 21'
    },
    {
        'author': 'chaindraa wahid',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 22'

    },
    {
        'author': 'habibi fouad',
        'title': 'Blog for fouad 2',
        'content': ' first blog for test fouad it is hardcoded',
        'date_posted': 'Mai 30'

    },
    {
        'author': 'ghazali fatima',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 29'

    },
    {
        'author': 'chaindraa wahid',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 22'

    }
]


@application.route('/')
@application.route('/home')
def home():
    return render_template('index.html', posts=posts)


@application.route('/about')
def about():
    return render_template('about.html', title='About')


@application.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    form = Sign_up()
    if form.validate_on_submit():
        password_hashed = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=password_hashed)
        db.session.add(user)
        db.session.commit()
        flash('Mr : {} Your Account was created successfully you are able to log in Now'.format(
            form.username.data), 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Sign_up', form=form)


@application.route('/login', methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.rememberMe.data)
            return redirect(url_for('home'))
        else:
            flash('logged in unsuccessfull, You must check your username or password')
    return render_template('login.html', title='Login', form=form)
