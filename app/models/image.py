from .db import db

class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    url = db.Column(db.String(500))

    reviews = db.relationship('Review', back_populates='images')
    business = db.relationship('Business', back_populates='images')

    def to_dict(self):
        return {
            "id": self.id,
            "review_id": self.review_id,
            "business_id": self.business_id,
            "url": self.url
        }
