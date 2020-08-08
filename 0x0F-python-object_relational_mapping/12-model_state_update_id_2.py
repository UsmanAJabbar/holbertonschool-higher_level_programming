#!/usr/bin/python3
"""Updates ID(2) to New Mexico"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    # Connect to the database
    user, passwd, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.\
                           format(user, passwd, database), pool_pre_ping=True)

    # Bind the database details and create a session
    Session = sessionmaker(bind = engine)
    session = Session()

    # Fetch the ID assigned to new_state
    results = session.query(State).filter(State.id == 2).all()

    # Check if results aren't empty and update if so, then commit
    if results != []:
        results[0].name = 'New Mexico'
        session.commit()
