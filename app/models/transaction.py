from .db import db


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    transaction = db.Column(db.String(50))

    b_transactions = db.relationship(
        'Business',
        secondary='business_transactions',
        back_populates='business_t'
    )


def to_dict(self):
    return {
        "id": self.id,
        "business_id": self.business_id,
        "transation": self.transation,
    }
