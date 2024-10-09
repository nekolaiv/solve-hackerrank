#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    return sum(map(lambda x: x, ar))

if __name__ == '__main__':

    ar = list(map(int, input(f"Type and Separate numbers by spaces: ").rstrip().split()))

    result = aVeryBigSum(ar)

    print(f"Sum: {result}")
