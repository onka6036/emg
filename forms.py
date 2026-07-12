from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Optional


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class BookingForm(FlaskForm):
    course_title = SelectField('Training Program', choices=[('Information Technology', 'Information Technology'), ('Networking', 'Networking'), ('Cybersecurity', 'Cybersecurity'), ('Microsoft Office', 'Microsoft Office'), ('Cloud Computing', 'Cloud Computing')], validators=[DataRequired()])
    trainer = StringField('Preferred Instructor', validators=[Optional()])
    booking_date = StringField('Preferred Date', validators=[DataRequired()])
    booking_time = StringField('Preferred Time', validators=[DataRequired()])
    training_type = SelectField('Training Type', choices=[('Online', 'Online'), ('On-site', 'On-site')], validators=[DataRequired()])
    notes = TextAreaField('Additional Details', validators=[Optional()])
    submit = SubmitField('Request Booking')
