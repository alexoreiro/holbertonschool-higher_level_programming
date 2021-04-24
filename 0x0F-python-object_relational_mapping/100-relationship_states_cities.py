#!/usr/bin/python3
""" Documentation """
from sys import argv
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    if (len(argv) == 4):
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, dbname), pool_pre_ping=True)
        Base.metadata.create_all(bind=engine, checkfirst=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        california = State(name='California')
        city = City(name='San Francisco', state=california)
        session.add(city)
        session.commit()
        session.close()
