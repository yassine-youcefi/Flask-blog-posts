from flask import render_template, url_for, flash, redirect, request
from app.forms import Sign_up, Login
from app.models import User, Post
from app import application, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    # check if user is already authenticated
    if current_user.is_authenticated:
        redirect(url_for('home'))

    # get the sign_up form
    form = Sign_up()
    # validate the forme when on submit
    if form.validate_on_submit():
        # hash the password
        password_hashed = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        # create the user
        user = User(username=form.username.data,
                    email=form.email.data, password=password_hashed)
        db.session.add(user)
        db.session.commit()
        # render flash message
        flash('Mr : {} Your Account was created successfully you are able to log in Now'.format(
            form.username.data), 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Sign_up', form=form)


@application.route('/login', methods=["GET", "POST"])
def login():
    # check if user is already authenticated
    if current_user.is_authenticated:
        redirect(url_for('home'))
    # get the login form
    form = Login()
    # check if the form is validate
    if form.validate_on_submit():
        # check if user exist on login
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # log in user
            login_user(user, remember=form.rememberMe.data)
            next_route = request.args.get('next')
            return redirect(next_route) if next_route else redirect(url_for('home'))
        else:
            flash(
                'logged in unsuccessfull, You must check your username or password', 'danger')
    return render_template('login.html', title='Login', form=form)


@application.route('/logout')
def logout():
    # logout user
    logout_user()
    return redirect(url_for('home'))


# user must be logged in
@application.route('/profile')
@login_required
def profile():
    user_profile = url_for(
        'static', filename='images/' + current_user.image_file)
    return render_template('profile.html', title='profile', image_file=user_profile)
