from .db import db
from .business_type import BusinessType

class Type(db.Model):
    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(500))
    alias = db.Column(db.String(500))


    b_types = db.relationship(
        'Business',
        secondary=BusinessType,
        back_populates='business_ty'
    )


    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "alias": self.alias
        }