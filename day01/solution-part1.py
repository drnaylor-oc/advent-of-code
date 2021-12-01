#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# Load the data from the file
data = np.loadtxt("1-1input.txt")

# We shift the array by one to the left (index 1 becomes 0)
# and we remove the final entry as that would be last entry
# minus first entry (and we don't care for that)
diff = (np.roll(data, -1) - data)[0:-1]

# if the number is positive, we count it, 
# diff > 0 returns an array of booleans that
# indicates if each element passed the predicate,
# putting this into the index operator for a numpy
# array returns only the elements that passed,
# and we get the size.
print(diff[diff > 0].size)


