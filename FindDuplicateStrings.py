
#==================================================================================================
#==================================================================================================
#
# Title: The Find Duplicate Strings Project
#
#==================================================================================================
#==================================================================================================

import asyncio
import time, datetime
import random

method_elapsed_time = []

strData = ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP01","ABCD5", "DUP02", "ABCD7","DUP02"]
solutionData = [[3, 4], [6,8]]

def FindDupStrings_Method(methNum):
    dtStart = datetime.datetime.now()

    # Sleep a random time inplace of find dup str code
    ranNum = random.randint(1,9)
    print(f" M{methNum} random int: {ranNum}")
    time.sleep(ranNum)

    dtEnd = datetime.datetime.now()
    method1_elapsed_time = dtEnd - dtStart    
    return dtEnd - dtStart


async def main():
    print("Main start")
    print()
    method_elapsed_time.append(FindDupStrings_Method(1))
    method_elapsed_time.append(FindDupStrings_Method(2))

    i = 0
    for elapse_time in method_elapsed_time:
        i = i + 1
        print(f"*** Elapsed Time for method {i} is {elapse_time} in seconds ***")

asyncio.run(main())

