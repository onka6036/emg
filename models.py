from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    full_name = db.Column(db.String(120), default='')
    phone = db.Column(db.String(40), default='')
    profile_photo = db.Column(db.String(255), default='')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.String(40), default='')
    requirements = db.Column(db.Text, default='')
    learning_outcomes = db.Column(db.Text, default='')
    certification = db.Column(db.String(120), default='')
    overview = db.Column(db.Text, default='')
    featured = db.Column(db.Boolean, default=False)
    published = db.Column(db.Boolean, default=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    course_title = db.Column(db.String(150), nullable=False)
    trainer = db.Column(db.String(100), default='')
    booking_date = db.Column(db.String(40), nullable=False)
    booking_time = db.Column(db.String(40), nullable=False)
    training_type = db.Column(db.String(50), default='Online')
    status = db.Column(db.String(20), default='Pending')
    notes = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), default='')
    content = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=True)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(40), default='')
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=True)


class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    published = db.Column(db.Boolean, default=True)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(50), default='bi-stars')
    published = db.Column(db.Boolean, default=True)


class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), default='')
    bio = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=True)
