from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, DataRequired, Email, EqualTo, ValidationError, Regexp
from app.models import User

class FeedbackForm(FlaskForm):
    name = StringField('Your Name', validators=[InputRequired(), Length(max=50)], render_kw={"class": "form-control"})
    message = TextAreaField('Your Feedback', validators=[InputRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Submit Feedback', render_kw={"class": "btn btn-primary"})

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Це імя користувача вже зайняте.Виберіть інше.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Цей email вже зареєстрований. Використайте інший.')

    def validate_usernameformat(self, username):
        if not Regexp(r'^[a-zA-Z0-9]+$', message='Імя користувача може містити лише літери, цифри та знак підкреслення.')(self, username):
            raise ValidationError('Імя користувача може містити лише літери, цифри та знак підкреслення. ')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
