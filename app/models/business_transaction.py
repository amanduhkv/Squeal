from .db import db

Business_Transaction = db.Table(
    'business_transactions',
    db.Model.metadata,
    db.Column('business_id', db.Integer, db.ForeignKey(
        'businesses.id'), primary_key=True),
    db.Column('transaction_id', db.Integer, db.ForeignKey(
        'transactions.id'), primary_key=True, nullable=False)
)