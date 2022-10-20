from .db import db

business_types = db.Table(
    'business_types',
    db.Model.metadata,
    db.Column('business_id', db.Integer, db.ForeignKey(
        'businesses.id'), primary_key=True),
    db.Column('type_id', db.Integer, db.ForeignKey(
        'types.id'), primary_key=True)
)

business_transactions = db.Table(
    'business_transactions',
    db.Model.metadata,
    db.Column('transaction_id', db.Integer, db.ForeignKey(
        'transactions.id'), primary_key=True),
    db.Column('business_id', db.Integer, db.ForeignKey(
        'businesses.id'), primary_key=True),
)

class Business(db.Model):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    price_range = db.Column(db.String, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)
    preview_img = db.Column(db.String)
    phone_number = db.Column(db.String(25))

    owner = db.relationship('User', back_populates='business')
    review = db.relationship('Review', back_populates='business')
    images = db.relationship('Image', back_populates='business')

    types = db.relationship(
        'Type',
        secondary=business_types,
        back_populates="businesses"
    )

    transactions = db.relationship(
        'Transaction',
        secondary=business_transactions,
        back_populates='businesses'
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
            "end_time": self.end_time,
            # "types": self.types,
            # "transactions": self.transactions
        }


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    transaction = db.Column(db.String(50))

    businesses = db.relationship(
        'Business',
        secondary=business_transactions,
        back_populates='transactions'
    )

    def to_dict(self):
        return {
            "id": self.id,
            # "business_id": self.business_id,
            "transaction": self.transaction,
        }


class Type(db.Model):
    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(500))
    alias = db.Column(db.String(500))

    businesses = db.relationship(
        'Business',
        secondary=business_types,
        back_populates='types'
    )

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "alias": self.alias
        }
