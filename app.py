from flask import Flask, render_template, url_for
from flask import flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import Sign_up, Login
from config import Config
from models import User, Post

application = Flask(__name__)


# application config "object"
application.config.from_object(Config)

# init database instance
db = SQLAlchemy(application)
migrate = Migrate(application, db)

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
        flash('Mr : {} Your Account was created successfully'.format(
            form.username.data), 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Sign_up', form=form)


@application.route('/login', methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.username.data == "yani" and form.password.data == "password":
            flash('Mr : {} You are logged in '.format(
                form.username.data), 'success')
            return redirect(url_for('home'))
        else:
            flash('logged in unsuccessfull, You must check your username or password')
    return render_template('login.html', title='Login', form=form)


# if __name__ == "__main__":
#     application.run(debug=True, port=5050)
