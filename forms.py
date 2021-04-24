from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Registration(Flaskform):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=4, max=255)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign_up')


class Login(Flaskform):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=4, max=255)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    rememberMe = BooleanField('Remmember Me')
    submit = SubmitField('Sign_up')

