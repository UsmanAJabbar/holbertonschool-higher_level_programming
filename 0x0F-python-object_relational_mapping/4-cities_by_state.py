#!/usr/bin/python3
"""Prints the data found in the states table"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    # Rename and set the varibles for readability
    user, passwd, database = argv[1], argv[2], argv[3]

    # Plug in the values
    db = MySQLdb.connect('localhost', user, passwd, database)

    # Create a cursor to navigate the database
    lookup = db.cursor()

    # Use the cursor to execute the command
    lookup.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities INNER JOIN states\
                    ON cities.state_id=states.id")

    # Fetch all the data
    ma_dayta = lookup.fetchall()

    # Print out the data fetched
    for cities in ma_dayta:
        print(cities)

    # Cleanup
    lookup.close()
    db.close()
