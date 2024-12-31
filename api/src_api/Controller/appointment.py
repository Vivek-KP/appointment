from flask import Blueprint,request,jsonify
from src_api.models.TimeSlot import TimeSlot
from src_api.models.BookingDetails import BookingDetails
from src_api import db
from datetime import datetime


slot_bp = Blueprint('eg',__name__)

class Appointment:
    @slot_bp.route('/',methods=['GET'])
    def getAllSlot():
        timeSlots = TimeSlot.query.all()
        result = []
        for timeSlot in timeSlots:
            data = timeSlot.slotDetails()
            result.append(data)
        print(result)
        return result
    

    
    @slot_bp.route('/',methods=['POST'])
    def bookASlot():
        data = request.get_json()
        if not data:
            return jsonify({'status': 'FAIL', 'message': 'Invalid or missing data'})
        else:
            print(data)
            bookSlot = BookingDetails(
                name = data['name'],
                phone = data['phone'],
                date = datetime.strptime(data['date'], '%Y-%m-%d').date(),
                time_slot_id = data['time_slot_id']
            )
            db.session.add(bookSlot)
            db.session.commit()
            return bookSlot.bookingDetails()
