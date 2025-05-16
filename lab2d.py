#!/usr/bin/env python3

import sys

# Check if exactly 2 arguments are provided, set to 3 because the original running python script also count as 1 argument
if len(sys.argv) != 3:
    print("Usage:", str(sys.argv[0]), "name age")
    sys.exit(0)

# Assign arguments to objects
name = sys.argv[1]
age = sys.argv[2]
print('Hi', name+ ', you are' , str(age) , 'years old.')


