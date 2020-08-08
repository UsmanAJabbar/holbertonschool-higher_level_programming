#!/usr/bin/python3
"""All States via Alchemy"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from model_city import City

    # Connect to the database
    user, passwd, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database), pool_pre_ping=True)

    # Bind the database details and create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Join the necessary tables accordingly
    result = session.query(City, State).join(State,
                                             City.state_id == State.id).all()

    # Loop through both of them
    for cities, states in result:
        print('{}: ({}) {}'.format(states.name, cities.id, cities.name))
