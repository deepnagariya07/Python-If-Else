Task
Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Output Format

# Print Weird if the number is weird; otherwise, print Not Weird.
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
# attempt 4
    if n % 2 != 0:
        print("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
    
    
    
    
	#attempt 3    
    # if n % 2 == False:
    #     print('wierd')
    # elif n % 2 == 0 and range(6,21):
    #     print('wierd')
    # elif n % 2 == 0 and range(2,6) or n >20:
    #     print('not wierd')
    #     break
    
    
    
    #attempt2
    # if n % 2 != 0:
    #     #continue
    #     print('Weird')
    # elif n % 2 == 0 and 2 >= n <= 5:
    #     print('Not Weird')
    #    # continue
    # elif n % 2 == 0 and 6 >= n <= 20:
    #     print('Weird')
    #   #continue
    # elif n % 2 == 0 and n >= 20:
    #     #continue
    #     print('Not Weird')
    # else:
    #     pass

    #attempt1
    # if n % 2 == 0 and range(2,5):
    #     print('Not Weird')
    # elif n % 2 == 0 and range(6,21):
    #     print('Weird')
    # elif n % 2 == 0 and n >= 21:
    #     print('Not Weird')
    # elif n % 2 != 0:
    #     print('Weird')       
    # else:
    #     pass           
