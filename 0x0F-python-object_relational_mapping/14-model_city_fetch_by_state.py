#!/usr/bin/python3
''' list objects from State '''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    que = session.query(State.name, City.id, City.name)
                         .filter(State.id == City.state_id)
    for ins in que:
        print(ins[0] + ": (" + str(ins[1]) + ") " + ins[2])
