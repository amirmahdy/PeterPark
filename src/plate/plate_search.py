from flask import Blueprint
from plate.models import Plates
import app.database as database
from flask import request
from app.exception_handler import unpredicted_exception_handler

bp = Blueprint('plate_search', __name__)


@bp.route('/search-plate', methods=['GET'])
@unpredicted_exception_handler('DEBUG')
def index():
    key = request.args.get('key', None)
    levenshtein = request.args.get('levenshtein', 0)

    plates = database.search_lev(Plates, search_text=key, lv_dist=levenshtein)

    all_plates = []
    for plate in plates:
        all_plates.append({
            "plate": plate.plate,
            "timestamp": plate.timestamp,
        })
    return all_plates, 200
