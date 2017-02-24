from models import *

db.create_all()

db.session.add(User("dinocala","96kalkon@gmail.com",34))
db.session.add(User("James","james@gmail.com",55))
db.session.add(User("George","geo1992@gmail.com",1))
db.session.add(User("Mary","strawberry69@gmail.com",23))
db.session.add(User("Sotiris","sotos888@gmail.com",13))
db.session.add(User("Alexander","alex.grimes@gmail.com",19))
db.session.add(User("Wayne","pp2017a@gmail.com",33))
db.session.add(User("Jacob","jacobjonas@gmail.com",90))

db.session.commit()