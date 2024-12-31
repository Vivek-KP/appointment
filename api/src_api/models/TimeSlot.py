from src_api import db
from sqlalchemy.sql import func


class TimeSlot(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    slot = db.Column(db.String(250),nullable = False)
    created_date = db.Column(db.DateTime,default = func.now())
    updated_date = db.Column(db.DateTime,default = func.now(),onupdate = func.now())

    def slotDetails(self):
        return {
        'id': self.id,
        'slot': self.slot
    }