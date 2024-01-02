from flask import Blueprint

blueprint = Blueprint('common', __name__, url_prefix='/common')


# the minimal Flask application
@blueprint.route('/')
@blueprint.route('/hello')
def index():
    return 'Hello, I am common'


# dynamic route, URL variable default
@blueprint.route('/greet', defaults={'name': 'Anonymous'})
@blueprint.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'
