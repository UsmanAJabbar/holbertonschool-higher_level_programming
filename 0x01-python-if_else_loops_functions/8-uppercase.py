#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        # Update switch every time you need to
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            switch = (ord(str[i]) - 32)
        else:
            switch = ord(str[i])
	# Print the updated value of switch
        print("{:c}".format(switch), end='')
    print("")
