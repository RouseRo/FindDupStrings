
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

dupStringTestData = []

class DuplicateStringsResults:
    def __init__(self, elapsed_time, indexList):
        self.elapsed_time = elapsed_time
        self.indexList = indexList

    def IsValidResult(self, expectedIndexList):
        if expectedIndexList ==   self.indexList:
            return True
        else:
            return False


class DuplicateStringTestData:
    def __init__(self, name, testDataList, solutionList):
        self.name = name
        self.testDataList = testDataList
        self.solutionList = solutionList

def FindDupStrings_Method(methNum):
    dtStart = datetime.datetime.now()

    # Sleep a random time inplace of find dup str code
    ranNum = random.randint(1,5)
    print(f" M{methNum} random int: {ranNum}")
    time.sleep(ranNum)

    dtEnd = datetime.datetime.now()
    method_elapsed_time = dtEnd - dtStart 
    return DuplicateStringsResults(method_elapsed_time,solutionData)

def FindDupStrings_MethodPassedData(methNum, DuplicateStringTestData):

    methodResults = FindDupStrings_Method(methNum)
    if methodResults.indexList == DuplicateStringTestData.solutionList:
        resultStr = "PASS"
    else:
        resultStr = "FAIL"
    print(f" {resultStr}: Medthod: [{methNum}], Test Data Name: **{DuplicateStringTestData.name}**, Elapsed Time: {methodResults.elapsed_time}")
    return

async def main():
    print("Main start")

    # Build test data
    dupStringTestData.append(DuplicateStringTestData("No Dups", ["abcd1", "abcd2", "ABCD3"],[]))
    dupStringTestData.append(DuplicateStringTestData("One Dup Str", ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP01","ABCD5"],[3,4]))
    dupStringTestData.append(DuplicateStringTestData("Multiple Dup Strs", ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP01","ABCD5", "DUP02", "ABCD7","DUP02"],
                                                     [[3, 4], [6,8]]))

    print()

    # Run all the test data thru all the methods.
    for i in range(1,3):
        for testData in dupStringTestData:
                FindDupStrings_MethodPassedData(i, testData)
                print()

    print()

asyncio.run(main())

