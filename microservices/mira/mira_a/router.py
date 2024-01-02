from flask import Blueprint

blueprint = Blueprint("mira_a", __name__, url_prefix='/a')


@blueprint.route('/')
def index():
    return 'I am Mira A'


@blueprint.route('/details')
def details():
    return 'I am Mira A Details'
