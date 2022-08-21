from app import create_app
from plate.plate_get import bp as plate_get_bp
from plate.plate_post import bp as plate_post_bp
from plate.plate_search import bp as plate_search_bp
from app.swagger import swaggerui_bp
from app.static import bp as static_file_get_bp

app = create_app()
app.register_blueprint(plate_get_bp)
app.register_blueprint(plate_post_bp)
app.register_blueprint(plate_search_bp)

app.register_blueprint(swaggerui_bp)
app.register_blueprint(static_file_get_bp)