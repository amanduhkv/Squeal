from .db import db
from sqlalchemy import func
from datetime import datetime


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    review_body = db.Column(db.String(5000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String, default=datetime.now)
    updated_at = db.Column(
        db.String, default=datetime.now, onupdate=datetime.now)
    # updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = db.relationship('User', back_populates='review')
    business = db.relationship('Business', back_populates='review')
    images = db.relationship('Image', back_populates='reviews')

    def to_dict(self):
        return {
            "id": self.id,
            "business_id": self.business_id,
            "user_id": self.user_id,
            # ^double check if this is correct
            "review_body": self.review_body,
            "rating": self.rating,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
