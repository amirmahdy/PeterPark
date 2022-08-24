from flask import Blueprint
from plate.models import Plates
from flask import request
import app.database as database
from plate.validator import validate_plate
from app.exception_handler import unpredicted_exception_handler

bp = Blueprint('plate_post', __name__)


@bp.route('/plate', methods=['POST'])
@unpredicted_exception_handler('DEBUG')
def index():
    data = request.get_json()
    validated_data = validate_plate(data)

    if validated_data is None:
        return "Malformed Request", 400

    elif validated_data == False:
        return "Wrong format", 422

    else:
        database.insert_instance(Plates, plate=data['plate'])
    return "Done", 200
