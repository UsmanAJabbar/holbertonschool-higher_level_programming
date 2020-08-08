#!/usr/bin/python3
"""Takes in a search query and returns the id if it exists"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    # Connect to the database
    user, passwd, database, search_term = argv[1], argv[2], argv[3], argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database), pool_pre_ping=True)

    # Bind the database details and create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch results by generating a query
    results = session.query(State).filter(State.name == search_term).all()

    if results:
        for states in results:
            print('{}'.format(states.id))
    else:
        print('Not Found')
