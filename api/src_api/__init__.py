from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def create_app():
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointment.db'
        db.init_app(app)

        from src_api.models.TimeSlot import TimeSlot
        from src_api.models.BookingDetails import BookingDetails

        from src_api.Controller.appointment import slot_bp
        from initialData import insert_timeslots
        app.register_blueprint(slot_bp)
        with app.app_context():
                db.create_all()
                insert_timeslots()

        return app





