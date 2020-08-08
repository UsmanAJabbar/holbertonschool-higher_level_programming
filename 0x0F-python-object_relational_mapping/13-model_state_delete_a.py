#!/usr/bin/python3
"""Deletes All States that have an 'a' in them"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    # Connect to the database
    user, passwd, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database), pool_pre_ping=True)

    # Bind the database details and create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Pulls out all the states with an 'a' in them
    result = session.query(State).filter(State.name.like('%a%')).all()

    # Loop through and delete all of them individually
    for states in result:
        session.delete(states)

    # Commit changes
    session.commit()
