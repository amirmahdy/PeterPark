from flask import Blueprint
from plate.models import Plates
import app.database as database
from app.exception_handler import unpredicted_exception_handler

bp = Blueprint('plate_get', __name__)


@bp.route('/plate', methods=['GET'])
@unpredicted_exception_handler('DEBUG')
def index():
    plates = database.get_all(Plates)
    all_plates = []
    for plate in plates:
        all_plates.append({
            "plate": plate.plate,
            "timestamp": plate.timestamp,
        })
    return all_plates, 200
