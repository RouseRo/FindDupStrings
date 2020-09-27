
#==================================================================================================
#==================================================================================================
#
# Title: The Find Duplicate Strings Project
# Author: Robert Rouse
# Created Date: 09-11-2020, 12:15
# Last Update:  09-14-2020, 16:32
#
# History:
#   Added the DuplicateStringsResults class
#   Added the DuplicateStringTestData class and the FindDupStrings_MethodPassedData()
#   Added Calling FDS_Methods by function number
#   Adding the Hash method
#
#==================================================================================================
#==================================================================================================

import asyncio
import time, datetime
import random
import collections
import hashlib

solutionData  = [[3, 4], [6,8]]

dupStringTestData = []
hashTable = []
hashTableSize = 200

class DuplicateStringsResults:
    def __init__(self, methodName, elapsed_time, indexList):
        self.methodName = methodName
        self.elapsed_time = elapsed_time
        self.indexList = indexList

    def IsValidResult(self, expectedIndexList):
        if expectedIndexList ==   self.indexList:
            return True
        else:
            return False


class DuplicateStringTestData:
    def __init__(self, name, testDataList, solutionLists):
        self.name = name
        self.testDataList = testDataList
        self.solutionLists = solutionLists

def FindDupStrings_Random_Method():
    dtStart = datetime.datetime.now()

    # Sleep a random time inplace of find dup str code
    ranNum = random.randint(1,5)
    # print(f" random int: {ranNum}")
    time.sleep(ranNum)

    dtEnd = datetime.datetime.now()
    method_elapsed_time = dtEnd - dtStart 
    return DuplicateStringsResults("Random", method_elapsed_time,solutionData)


def FindDupStrings_Hash_Method(DuplicateStringTestData):
    solutionLists = []
    unique_dup_strs = 0

    dtStart = datetime.datetime.now()
    solutionLists.clear()

    hashTable.clear()
    for i in range(hashTableSize):
        hashTable.append(0)

    print(f"len of hashTable {len(hashTable)}")

    pos = -1
    for str2hash in DuplicateStringTestData.testDataList:
        solutionLists.append(pos)
        pos = pos + 1
        hashIndex = abs(hash(str2hash)) % hashTableSize
        print(f"str[{str2hash}] hash index:[{hashIndex}]")
        hashTable[hashIndex] = hashTable[hashIndex] + 1
        if hashTable[hashIndex] > 1:
            print(f" {str2hash} {hashTable[hashIndex]} is a duplicate")

            # Is this a string the same as the previous 

            solutionLists.append(pos)
        else:
            solutionLists.pop()

    dtEnd = datetime.datetime.now()
    method_elapsed_time = dtEnd - dtStart 
    return DuplicateStringsResults("Hash", method_elapsed_time,solutionLists)

def FindDupStrings_Set_Method(DuplicateStringTestData):
    method_elapsed_time = 2
    return DuplicateStringsResults("Set", method_elapsed_time,solutionData)

def FindDupStrings_Dict_Method(DuplicateStringTestData):
    method_elapsed_time = 3
    return DuplicateStringsResults("Dict", method_elapsed_time,solutionData)



def FindDupStrings_MethodPassedData(funcNum, DuplicateStringTestData):
    if funcNum == 1:
        methodResults = FindDupStrings_Random_Method()

    if funcNum == 2:
        methodResults = FindDupStrings_Hash_Method(DuplicateStringTestData)

    if funcNum == 3:
        methodResults = FindDupStrings_Set_Method(DuplicateStringTestData)

    if funcNum == 4:
        methodResults = FindDupStrings_Dict_Method(DuplicateStringTestData)


    print(f"Solution Lists: {DuplicateStringTestData.solutionLists} Method Lists: {methodResults.indexList}")
    if methodResults.indexList == DuplicateStringTestData.solutionLists:
        resultStr = "PASS"
    else:
        resultStr = "FAIL"
    print(f" {resultStr}: Medthod: [{methodResults.methodName}], Test Data Name: **{DuplicateStringTestData.name}**, Elapsed Time: {methodResults.elapsed_time}")
    return

async def main():
    print("Main start")

    # Build test data
    dupStringTestData.append(DuplicateStringTestData("No Dups", ["abcd1", "abcd2", "ABCD3"],[]))
    dupStringTestData.append(DuplicateStringTestData("One Dup Str 1", ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP01","ABCD5"],[3,4]))
    dupStringTestData.append(DuplicateStringTestData("One Dup Str 2", ["abcd1", "DUP01", "abcd2", "ABCD3", "DUP01","ABCD5"],[1,4]))
    dupStringTestData.append(DuplicateStringTestData("Multiple Dup Strs", ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP01","ABCD5", "DUP02", "ABCD7","DUP02"],
                                                     [[3, 4], [6,8]]))

    print()

    # Run all the test data thru all the methods.
    for i in range(2,3):
        for testData in dupStringTestData:
                FindDupStrings_MethodPassedData(i, testData)
                print()

    print()

asyncio.run(main())

