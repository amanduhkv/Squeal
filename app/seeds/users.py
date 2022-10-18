# import bcrypt
from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    owner1 = User(username="9ziggy9",
                  email="davidrogers@user.io",
                  password="password",
                  first_name="David",
                  last_name="Rogers",
                  profile_pic="https://emoji.slack-edge.com/T03GU501J/zoomcrashed/b828461faedcbc70.png")

    owner2 = User(first_name='Adam',
                  last_name='Selki',
                  email='adamselki@user.io',
                  username='adamselki',
                  password='password',
                  profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"
                  )

    owner3 = User(first_name='Aijia',
                  last_name='Wang',
                  email='aijiawang@user.io',
                  username='aijiawang',
                  password='password',
                  profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                  )
    owner4 = User(first_name='Alexander',
                  last_name='Klivecka',
                  email='alexanderklivecka@user.io',
                  username='alexanderklivecka',
                  password='password',
                  profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                  )
    owner5 = User(first_name='Andrea',
                  last_name='Wu',
                  email='andreawu@user.io',
                  username='andreawu',
                  password='password',
                  profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                  )
    owner6 = User(first_name='Brandon',
                  last_name='Tasaki',
                  email='brandontasaki@user.io',
                  username='brandontasaki',
                  password='password',
                  profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                  )
    owner7 = User(first_name='Christopher',
                  last_name='Pannella',
                  email='christopherpannella@user.io',
                  username='christopherpannella',
                  password='password',
                  profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                  )
    owner8 = User(first_name='Jacob',
                  last_name='Lamar',
                  email='jacoblamar@user.io',
                  username='jacoblamar',
                  password='password',
                  profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"
                  )
    owner9 = User(first_name='Jae',
                  last_name='Hwang',
                  email='jaehwang@user.io',
                  username='jaehwang',
                  password='password',
                  profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                  )
    owner10 = User(first_name='Jake',
                   last_name='Matillano',
                   email='jakematillano@user.io',
                   username='jakematillano',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner11 = User(first_name='James',
                   last_name='Lee',
                   email='jameslee@user.io',
                   username='jameslee',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner12 = User(first_name='Jason',
                   last_name='Kong',
                   email='jasonkong@user.io',
                   username='jasonkong',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner13 = User(first_name='Jason',
                   last_name='Arnold',
                   email='jasonarnold@user.io',
                   username='jasonarnold',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner14 = User(first_name='Jessie',
                   last_name='Baron',
                   email='jessiebaron@user.io',
                   username='jessiebaron',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner15 = User(first_name='Joanna',
                   last_name='Gilbert',
                   email='joannagilbert@user.io',
                   username='joannagilbert',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner16 = User(first_name='John',
                   last_name='Carrera',
                   email='johncarrera@user.io',
                   username='johncarrera',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner17 = User(first_name='Logan',
                   last_name='Seals',
                   email='loganseals@user.io',
                   username='loganseals',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner18 = User(first_name='Keerthana',
                   last_name='Yellapragada',
                   email='keerthanayellapragada@user.io',
                   username='keerthanayellapragada',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner19 = User(first_name='Kyle',
                   last_name='Kassen',
                   email='kylekassen@user.io',
                   username='kylekassen',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner20 = User(first_name='Michael',
                   last_name='Jung',
                   email='michaeljung@user.io',
                   username='michaeljung',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner21 = User(first_name='Na',
                   last_name='Chen',
                   email='nachen@user.io',
                   username='nachen',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner22 = User(first_name='Samuel',
                   last_name='Suh',
                   email='samuelsuh@user.io',
                   username='samuelsuh',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner23 = User(first_name='Schaeffer',
                   last_name='Ahn',
                   email='schaefferahn@user.io',
                   username='schaefferahn',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner24 = User(first_name='Sean',
                   last_name='Kennedy',
                   email='seankennedy@user.io',
                   username='seankennedy',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner25 = User(first_name='Amanda',
                   last_name='Vien',
                   email='amandavien@user.io',
                   username='amandavien',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner26 = User(first_name='Yasha',
                   last_name='Yang',
                   email='yashayang@user.io',
                   username='yashayang',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner27 = User(first_name='Yibo',
                   last_name='Guo',
                   email='yiboguo@user.io',
                   username='yiboguo',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"

                   )
    owner28 = User(first_name='Kermit',
                   last_name='Frog',
                   email='kermitfrog@user.io',
                   username='kermitfrog',
                   password='password',
                   profile_pic="https://images.unsplash.com/photo-1509512693283-8178ed23e04c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8a2VybWl0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"

                   )

    db.session.add(owner1)
    db.session.add(owner2)
    db.session.add(owner3)
    db.session.add(owner4)
    db.session.add(owner5)
    db.session.add(owner6)
    db.session.add(owner7)
    db.session.add(owner8)
    db.session.add(owner9)
    db.session.add(owner10)
    db.session.add(owner11)
    db.session.add(owner12)
    db.session.add(owner13)
    db.session.add(owner14)
    db.session.add(owner15)
    db.session.add(owner16)
    db.session.add(owner17)
    db.session.add(owner18)
    db.session.add(owner19)
    db.session.add(owner20)
    db.session.add(owner21)
    db.session.add(owner22)
    db.session.add(owner23)
    db.session.add(owner24)
    db.session.add(owner25)
    db.session.add(owner26)
    db.session.add(owner27)
    db.session.add(owner28)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
