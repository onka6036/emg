from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from models import User, Booking, ContactMessage, Course, Testimonial, BlogPost, FAQ, GalleryImage, Service, TeamMember
from forms import RegisterForm, LoginForm, BookingForm
from extensions import db


bp = Blueprint('main', __name__)


def register_routes(app, db):
    app.register_blueprint(bp)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data.lower()).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Welcome back.', 'success')
                return redirect(url_for('admin_dashboard' if user.is_admin else 'student_dashboard'))
            flash('Invalid email or password.', 'danger')
        return render_template('auth/login.html', form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            if User.query.filter_by(email=form.email.data.lower()).first():
                flash('An account with that email already exists.', 'warning')
            else:
                user = User(username=form.username.data, email=form.email.data.lower())
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                flash('Account created. You can now sign in.', 'success')
                return redirect(url_for('login'))
        return render_template('auth/register.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been signed out.', 'info')
        return redirect(url_for('home'))

    @app.route('/student-dashboard')
    @login_required
    def student_dashboard():
        bookings = Booking.query.filter_by(user_id=current_user.id).all()
        return render_template('student_dashboard.html', bookings=bookings)

    @app.route('/admin-dashboard')
    @login_required
    def admin_dashboard():
        if not current_user.is_admin:
            abort(403)
        bookings = Booking.query.order_by(Booking.created_at.desc()).all()
        contacts = ContactMessage.query.order_by(ContactMessage.created_at.desc()).limit(8).all()
        return render_template('admin_dashboard.html', bookings=bookings, contacts=contacts)

    @app.route('/admin/bookings/<int:booking_id>/<status>')
    @login_required
    def update_booking_status(booking_id, status):
        if not current_user.is_admin:
            abort(403)
        booking = Booking.query.get_or_404(booking_id)
        booking.status = status.title()
        db.session.commit()
        flash('Booking status updated.', 'success')
        return redirect(url_for('admin_dashboard'))

    @app.route('/book-training', methods=['GET', 'POST'])
    def book_training():
        form = BookingForm()
        if form.validate_on_submit():
            booking = Booking(
                user_id=current_user.id if current_user.is_authenticated else None,
                course_title=form.course_title.data,
                trainer=form.trainer.data or 'EMG Instructor',
                booking_date=form.booking_date.data,
                booking_time=form.booking_time.data,
                training_type=form.training_type.data,
                notes=form.notes.data,
            )
            db.session.add(booking)
            db.session.commit()
            flash('Your training request has been submitted. Our team will contact you shortly.', 'success')
            return redirect(url_for('home'))
        return render_template('book_training.html', form=form)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            if name and email and message:
                db.session.add(ContactMessage(name=name, email=email, phone=phone or '', message=message))
                db.session.commit()
                flash('Thank you for your message. We will follow up soon.', 'success')
                return redirect(url_for('contact'))
            flash('Please fill out the required fields.', 'danger')
        return render_template('contact.html')

    @app.route('/blog/<slug>')
    def blog_post(slug):
        post = BlogPost.query.filter_by(slug=slug, published=True).first_or_404()
        return render_template('blog_post.html', post=post)
