
#==================================================================================================
#==================================================================================================
#
# Title: The Find Duplicate Strings Project
# Author: Robert Rouse
# Date: 09-11-2020, 12:15
#
# History:
#   Added the DuplicateStringsResults class
#
#==================================================================================================
#==================================================================================================

import asyncio
import time, datetime
import random
import collections


strData = ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP01","ABCD5", "DUP02", "ABCD7","DUP02"]
solutionData  = [[3, 4], [6,8]]
solutionData2 = [[3, 5], [6,8]]

methodResults = []

class DuplicateStringsResults:
    def __init__(self, elapsed_time, indexList):
        self.elapsed_time = elapsed_time
        self.indexList = indexList

    def IsValidResult(self, expectedIndexList):
        if expectedIndexList ==   self.indexList:
            return True
        else:
            return False


def FindDupStrings_Method(methNum):
    dtStart = datetime.datetime.now()

    # Sleep a random time inplace of find dup str code
    ranNum = random.randint(1,5)
    print(f" M{methNum} random int: {ranNum}")
    time.sleep(ranNum)

    dtEnd = datetime.datetime.now()
    method_elapsed_time = dtEnd - dtStart 

    # Insert the elapsed time and solution-list
    methodResults.insert(methNum - 1, DuplicateStringsResults(method_elapsed_time,solutionData))
  
    return


async def main():
    print("Main start")
    print()

    expectedResults = DuplicateStringsResults(0, solutionData)

    FindDupStrings_Method(1)
    FindDupStrings_Method(2)

    print()
    i = 0
    for methResult in methodResults:
        i = i + 1
        print(f"*** Elapsed Time for method {i} is {methResult.elapsed_time} in seconds ***")

        if methResult.IsValidResult(solutionData):
            print(f"*** Method {i} is Valid ***")
        else:
            print(f"*** Method {i} is Not Valid ***")

        if methResult.IsValidResult(solutionData2):
            print(f"*** Method {i} is Valid ***")
        else:
            print(f"*** Method {i} is Not Valid ***")

    print()

asyncio.run(main())

