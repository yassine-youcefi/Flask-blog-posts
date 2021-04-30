from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class Sign_up(FlaskForm):
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

    def validation_username(self, username):
        # try to get user instance filter by user name
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Userneme already exist')

    def validation_email(self, email):
        # try to get user instance filter by user name
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist')


class Login(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=4, max=255)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    rememberMe = BooleanField('Remmember Me')
    submit = SubmitField('Login')
