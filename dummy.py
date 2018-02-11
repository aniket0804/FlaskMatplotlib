import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///test.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin@devils.com","admin")
session.add(user)
 
user = User("python@devils.com","python")
session.add(user)
 
user = User("devil@devils.com","devil")
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()
