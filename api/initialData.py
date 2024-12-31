from src_api.models.TimeSlot import TimeSlot
from src_api import db



def insert_timeslots():
    if not TimeSlot.query.first():
        timeslots = [
        TimeSlot(slot='10:00 AM'),
        TimeSlot(slot='10:30 AM'),
        TimeSlot(slot='11:00 AM'),
        TimeSlot(slot='11:30 AM'),
        TimeSlot(slot='12:00 PM'),
        TimeSlot(slot='12:30 PM'),
        TimeSlot(slot='02:00 PM'),
        TimeSlot(slot='02:30 PM'),
        TimeSlot(slot='03:00 PM'),
        TimeSlot(slot='03:30 PM'),
        TimeSlot(slot='04:00 PM'),
        TimeSlot(slot='04:30 PM'),

        ]
        db.session.add_all(timeslots)
        db.session.commit()