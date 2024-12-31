from src_api import db
from sqlalchemy.sql import func
from sqlalchemy import UniqueConstraint


class BookingDetails(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(250),nullable = False)
    phone = db.Column(db.String(250),nullable=False)
    date = db.Column(db.Date,nullable = False)
    time_slot_id  = db.Column(db.Integer,db.ForeignKey('time_slot.id'),nullable = False)
    created_date = db.Column(db.DateTime,default = func.now())
    updated_date = db.Column(db.DateTime,default = func.now(),onupdate = func.now())
    time_slot = db.relationship('TimeSlot', backref=db.backref('bookings', lazy=True))


    __table_args__ = (
        UniqueConstraint('date','time_slot_id', name='uq_time_slot_user'),
    )

    def bookingDetails(self):
        return {
        'id': self.id,
        'name': self.name,
        'phone': self.phone,
        'date': self.date,
        'timeSlot': self.time_slot.slotDetails()

    }