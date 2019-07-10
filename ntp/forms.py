from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ntp.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):

    usuario = StringField('Usuario',
                          validators=[DataRequired(),Length(min=4, max=15)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),Length(min=6, max=20)])
    confirm_password = PasswordField('Confirmar Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarte')

    def validate_username(self, usuario):
        user = User.query.filter_by(username=usuario.data).first()
        if user:
            raise ValidationError('Este nick ya existe en la base de datos.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Ya existe una cuenta registrada con este mail.')


class LoginForm(FlaskForm):

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),Length(min=6, max=20)])
    remember = BooleanField('Recordarme')
    submit = SubmitField('Log In')



class UpdateAccountForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Ese Nick ya existe.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Ese mail ya esta registrado en nuestra base de datos.')

class PostForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired()])
    content = TextAreaField('Contenido', validators=[DataRequired()])
    submit = SubmitField('Postear')

class CommentForm(FlaskForm):
    comment = TextAreaField('Respuesta', validators=[DataRequired()])
    submit = SubmitField("Contestar")

