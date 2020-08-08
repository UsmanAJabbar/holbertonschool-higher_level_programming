#!/usr/bin/python3
"""Prints the data found in the states table"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    # Rename and set the varibles for readability
    user, passwd, database, search = argv[1], argv[2], argv[3], argv[4]

    # Plug in the values
    db = MySQLdb.connect('localhost', user, passwd, database)

    # Create a cursor to navigate the database
    lookup = db.cursor()

    # Use the cursor to execute the command
    lookup.execute("SELECT * FROM states WHERE BINARY name='{}'".format(search))

    # Fetch all the data
    ma_dayta = lookup.fetchall()

    # Print out the data fetched
    for states in ma_dayta:
        print(states)

    # Cleanup
    lookup.close()
    db.close()
