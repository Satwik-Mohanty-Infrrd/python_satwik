
import modules as mp
courses= ['History', 'Math', 'Physics', 'Chemistry']

index= mp.find_index(courses, 'Math')
print(index)


from modules import find_index, test
import sys

index=find_index(courses, 'Math')
print(index)
print(test)


import datetime
import calendar

today= datetime.date.today()
print(today)


import os 
print(os.getcwd())
print(os.__file__)

import antigravity