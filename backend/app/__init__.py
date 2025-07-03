from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

from config import Config

from app.routes import patients_bp
from app.extensions import db, migrate

def create_app():
    app = OpenAPI(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_api(patients_bp)

    from app.models import Patient


    return app
