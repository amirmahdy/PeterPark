from flask import send_from_directory
from flask import Blueprint

bp = Blueprint('static_files', __name__)

@bp.route('/static/<path:path>', methods=['GET'])
def index(path):
    return send_from_directory('/src/app/static/', path), 200
