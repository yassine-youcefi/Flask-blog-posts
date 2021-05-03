from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

# class validator for signup route


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

    # methode to check if username exist or not
    def validation_username(self, username):
        # try to get user instance filter by user name
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Userneme already exist')

    # methode to check if username exist or not
    def validation_email(self, email):
        # try to get user instance filter by user name
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist')

# class validator for login route


class Login(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=4, max=255)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    rememberMe = BooleanField('Remmember Me')
    submit = SubmitField('Login')


class Update_profile(FlaskForm):

    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=4, max=255)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])

    submit = SubmitField('update')

    # methode to check if username exist or not
    def validation_username(self, username):
        if username.data != current_user.username:
            # try to get user instance filter by user name
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Userneme already exist')

    # methode to check if username exist or not
    def validation_email(self, email):
        if email.data != current_user.email:
            # try to get user instance filter by user name
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exist')
