from .db import db

class Business(db.Model):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    price_range = db.Column(db.String, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)

    phone_number = db.Column(db.String(10))

    owner = db.relationship('User', back_populates='business')
    review = db.relationship('Review', back_populates='business')
    images = db.relationship('Image', back_populates='business')

    business_ty = db.relationship(
        'Type',
        secondary='business_types',
        back_populates='b_types'
    )
    business_t = db.relationship(
        'Transaction',
        secondary='business_transactions',
        back_populates='b_transactions'
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
            # ^double check if this is correct
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "address": self.address,
            "zipcode": self.zipcode,
            "lat": self.lat,
            "lng": self.lng,
            "price_range": self.price_range,
            "phone_number": self.phone_number,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
