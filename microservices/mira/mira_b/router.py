from flask import Blueprint

blueprint = Blueprint("mira_b", __name__, url_prefix='/b')


@blueprint.route('/')
def index():
    return 'I am Mira B'


@blueprint.route('/details')
def details():
    return 'I am Mira B Details'
