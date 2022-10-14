from app.models import db, Business

def seed_businesses():
    business1 = Business(name="Ziggy's Fried Chicken",
                         owner_id=1,
                         city='Pinole',
                         state='California',
                         country='United States of America',
                         address='123 ABC St',
                         zipcode='94563',
                         lat=38.0044,
                         lng=127.0884,
                         price_range=1,
                         phone_number='(123) 456-7890',
                         start_time="8:00",
                         end_time="17:00"
                         )


    business2 = Business(name="Airborne Roasting",
                         owner_id=1,
                         city='Union City',
                         state='California',
                         country='United States of America',
                         address='33476 Alvarado-Niles Rd',
                         zipcode='94587',
                         lat=37.5934,
                         lng=122.0439,
                         price_range=2,
                         phone_number="(510) 952-8800",
                         start_time="8:00",
                         end_time="17:00"
                         )


    business3 = Business(name="Devout Coffee",
                         owner_id=1,
                         city='Fremont',
                         state='California',
                         country='United States of America',
                         address='37323 Niles Blvd',
                         zipcode='94536',
                         lat=37.5485,
                         lng=121.9886,
                         price_range=2,
                         start_time="8:00",
                         end_time="17:00"
                         )

                
    db.session.add(business1)
    db.session.add(business2)
    db.session.add(business3)
    db.session.commit()


def undo_businesses():
    db.session.execute('TRUNCATE businesses RESTART IDENTITY CASCADE;')
    db.session.commit()