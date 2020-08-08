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
    lookup.execute("SELECT cities.name\
                    FROM cities JOIN states\
                    ON cities.state_id = states.id\
                    WHERE states.name=%s\
                    ORDER BY states.id ASC;", (search,))

    # Fetch all the data
    ma_dayta = lookup.fetchall()

    # Print out the data fetched
    for cities in range(len(ma_dayta)):
        print(ma_dayta[cities][0], end='')
        if cities < len(ma_dayta) - 1:
            print(', ', end='')
    print()

    # Cleanup
    lookup.close()
    db.close()
