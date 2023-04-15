from flask import render_template, url_for, redirect

from . import frontend
from app.api.models import User, db


# custom 404 handler
@frontend.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@frontend.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


@frontend.route('/users/<int:id>', methods=['GET'])
def user_details(id):
    user = User.query.get_or_404(id)
    return render_template('user_details.html', user=user)


@frontend.route('/users/delete/<int:id>', methods=['POST'])
def user_delete(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('frontend.users'))