#!/usr/bin/python3
import hidden_4

# Import Guard
if __name__ == '__main__':
    output = dir(hidden_4)  # Holds all variables returned by dir
    char = 0  # To be used to check individual characters ahead

    # Loop to index through the list (aka arrays returned by dir)
    for words in range(len(output)):
        # Check if the first two characters are '__'
        # If '__' restart the loop and check for '__' in the next list
        if output[words][char] == '_' and output[words][char + 1] == '_':
            continue
        # Print out individual classes stored in output
        print("{}".format(output[words]))
