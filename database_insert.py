from database_sample import db
from database_sample import Key
import datetime

db.create_all()
key1 = Key(datetime.datetime.now(), datetime.datetime.now(), 'Freeman', True)
key2 = Key(datetime.datetime.now(), datetime.datetime.now(), 'Campus Police', False)

db.session.add(key1)
db.session.add(key2)
db.session.commit()