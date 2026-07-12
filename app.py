import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import current_user
from config import Config
from extensions import db, login_manager
from models import User, Course, Booking, Testimonial, BlogPost, ContactMessage, FAQ, GalleryImage, Service, TeamMember
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

register_routes(app, db)


def seed_data():
    if User.query.count() == 0:
        admin = User(username='admin', email='admin@emg.com', is_admin=True)
        admin.set_password('admin123')
        db.session.add(admin)
    if Course.query.count() == 0:
        courses = [
            Course(title='Information Technology', category='IT', duration='6 Weeks', requirements='Basic computer literacy', learning_outcomes='Gain foundational IT skills', certification='Certificate of Completion', overview='A hands-on introduction to modern IT operations.', featured=True, published=True),
            Course(title='Networking', category='Networking', duration='8 Weeks', requirements='Basic networking awareness', learning_outcomes='Configure and troubleshoot networks', certification='Networking Certificate', overview='Deep dive into network administration and troubleshooting.', featured=True, published=True),
            Course(title='Cybersecurity', category='Security', duration='8 Weeks', requirements='Basic IT knowledge', learning_outcomes='Protect systems against threats', certification='Security Certificate', overview='Modern cybersecurity practices for professionals.', featured=True, published=True),
        ]
        db.session.add_all(courses)
    if Service.query.count() == 0:
        services = [
            Service(name='Computer Repair', description='Reliable repair and maintenance services', icon='bi-tools', published=True),
            Service(name='Corporate Training', description='Tailored employee training programs', icon='bi-people', published=True),
            Service(name='Computer Sales', description='Enterprise-grade workstation solutions', icon='bi-laptop', published=True),
        ]
        db.session.add_all(services)
    if Testimonial.query.count() == 0:
        db.session.add_all([
            Testimonial(author='Alicia M.', role='Operations Lead', content='The training transformed our team.', published=True),
            Testimonial(author='David T.', role='IT Manager', content='Professional, engaging, and highly relevant.', published=True),
        ])
    if BlogPost.query.count() == 0:
        db.session.add_all([
            BlogPost(title='How to Prepare Your Team for Cloud Adoption', slug='cloud-adoption', content='Cloud skills are essential for every modern organization.', published=True),
            BlogPost(title='Top Cybersecurity Habits for Remote Teams', slug='cybersecurity-habits', content='Protect your team with practical habits and tools.', published=True),
        ])
    if FAQ.query.count() == 0:
        db.session.add_all([
            FAQ(question='Do you offer on-site training?', answer='Yes, we provide both on-site and remote training.', published=True),
            FAQ(question='Can you support corporate clients?', answer='Absolutely. We tailor programs for businesses of all sizes.', published=True),
        ])
    if GalleryImage.query.count() == 0:
        db.session.add_all([
            GalleryImage(title='Training Session', image_url='/static/images/hero.jpg', published=True),
            GalleryImage(title='Repair Service', image_url='/static/images/hero.jpg', published=True),
        ])
    if TeamMember.query.count() == 0:
        db.session.add_all([
            TeamMember(name='Mina Johnson', role='Lead Instructor', bio='Experienced trainer in IT and leadership.', published=True),
            TeamMember(name='Carlos Reed', role='Technical Specialist', bio='Specializes in networking and support.', published=True),
        ])
    db.session.commit()


with app.app_context():
    db.create_all()
    seed_data()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    featured_courses = Course.query.filter_by(featured=True).limit(6).all()
    testimonials = Testimonial.query.filter_by(published=True).limit(3).all()
    blog_posts = BlogPost.query.filter_by(published=True).limit(3).all()
    faqs = FAQ.query.filter_by(published=True).limit(4).all()
    services = Service.query.filter_by(published=True).limit(6).all()
    return render_template('index.html', featured_courses=featured_courses, testimonials=testimonials, blog_posts=blog_posts, faqs=faqs, services=services)


@app.route('/about')
def about():
    team = TeamMember.query.filter_by(published=True).all()
    return render_template('about.html', team=team)


@app.route('/training-programs')
def training_programs():
    courses = Course.query.filter_by(published=True).all()
    return render_template('training_programs.html', courses=courses)


@app.route('/corporate-training')
def corporate_training():
    return render_template('corporate_training.html')


@app.route('/computer-sales')
def computer_sales():
    return render_template('computer_sales.html')


@app.route('/computer-repairs')
def computer_repairs():
    return render_template('computer_repairs.html')


@app.route('/services')
def services():
    services = Service.query.filter_by(published=True).all()
    return render_template('services.html', services=services)


@app.route('/gallery')
def gallery():
    images = GalleryImage.query.filter_by(published=True).all()
    return render_template('gallery.html', images=images)


@app.route('/testimonials')
def testimonials():
    items = Testimonial.query.filter_by(published=True).all()
    return render_template('testimonials.html', items=items)


@app.route('/blog')
def blog():
    posts = BlogPost.query.filter_by(published=True).all()
    return render_template('blog.html', posts=posts)


@app.route('/faq')
def faq():
    items = FAQ.query.filter_by(published=True).all()
    return render_template('faq.html', items=items)


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
