from app.models import Transaction,db

def seed_transactions():
    delivery = Transaction(transaction='delivery')
    pickup = Transaction(transaction='pickup')
    reservation = Transaction(transaction='restaurant_reservation')

    db.session.add(delivery)
    db.session.add(pickup)
    db.session.add(reservation)

    db.session.commit()

def undo_transations():
    db.session.execute('TRUNCATE transactions RESTART IDENTITY CASCADE;')
    db.session.commit()
