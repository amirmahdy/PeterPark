from app import db
from datetime import datetime


class Plates(db.Model):
    __tablename__ = 'plates'
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(12))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    @property
    def timestamp(self):
        return self.created.isoformat()

    def __repr__(self):
        return 'Plate: {0} at {1}'.format(self.plate, self.timestamp)
