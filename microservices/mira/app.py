from mscom import config
from flask import Flask, Blueprint

from .common import blueprint as common_bp
from .mira_a.router import blueprint as mira_a_bp
from .mira_b.router import blueprint as mira_b_bp

app = Flask(__name__)
app.register_blueprint(common_bp)
app.register_blueprint(mira_a_bp)
app.register_blueprint(mira_b_bp)

subcontext = "/subcontext"


@app.get('/')
def index():
    return 'Hello, World! I am a Flask app!'


@app.route('/details', methods=['GET', 'HEAD'])
def details():
    return 'I am a Flask app details'


@app.route(f'{subcontext}/details')
def sub_details():
    return 'I am a Flask app subcontext details'


@app.route(subcontext + '/view')
def sub_view():
    return 'I am a Flask app subcontext view'


blueprint = Blueprint("inner_bp", __name__, url_prefix='/inner_bp')
app.register_blueprint(blueprint, url_prefix="/xxx")


@blueprint.route('/some-sub-route', methods=["GET", "HEAD"])
def sub_route():
    return 'I am Sub Route'


@blueprint.post('/some-sub-route')
def sub_route():
    return 'I am Sub Route'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=config.microservice_settings.server_port)
