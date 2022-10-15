from .db import db

BusinessType = db.Table(
    'business_types',
    db.Model.metadata,
    db.Column('business_id', db.Integer, db.ForeignKey('businesses.id'), primary_key=True),
    db.Column('type_id', db.Integer, db.ForeignKey('types.id'), primary_key=True, nullable=False)
)