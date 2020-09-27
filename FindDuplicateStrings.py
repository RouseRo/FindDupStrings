
#==================================================================================================
#==================================================================================================
#
# Title: The Find Duplicate Strings Project
# Author: Robert Rouse
# Created Date: 09-11-2020, 12:15
# last Updated: 09-27-2020, 12:40
#
# History:
#   Added the DuplicateStringsResults class
#   Added the DuplicateStringTestData class and the FindDupStrings_MethodPassedData()
#   Added Calling FDS_Methods by function number
#   Adding the Hash method
#   Added GetFirstOccuranceOfStr()
#   The solution is now a list of lists.
#   Added GetIndexOfSolutionListWithDupStr()
#   Got the FindDupStrings_Set_Method() working
#   Remove Dictionary method and added Brute Force method
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

def GetFirstOccuranceOfStr(currentPos, testDataList):
    targetStr = testDataList[currentPos]
    for i in range(currentPos - 1, -1, -1):
        if testDataList[i] == targetStr:
            return i
    return -1

def GetIndexOfSolutionListWithDupStr(pos, solList, strList):
    solListsCount = len(solList)
    for i in range(solListsCount):
        if strList[solList[i][0]] == strList[pos]:
            return i
    return -1


def GetIndexOfSolutionListWithPos(pos, solList):
    solListsCount = len(solList)
    for i in range(solListsCount):
        if pos in solList[i]:
            return i

    return -1


#==================================================================================================
#==================================================================================================

def FindDupStrings_Random_Method():
    dtStart = datetime.datetime.now()

    # Sleep a random time inplace of find dup str code
    ranNum = random.randint(1,5)
    # print(f" random int: {ranNum}")
    time.sleep(ranNum)

    dtEnd = datetime.datetime.now()
    method_elapsed_time = dtEnd - dtStart 
    return DuplicateStringsResults("Random", method_elapsed_time,solutionData)

#==================================================================================================

def FindDupStrings_Hash_Method(DuplicateStringTestData):
    solutionLists = []

    dtStart = datetime.datetime.now()
    solutionLists.clear()

    hashTable.clear()
    for i in range(hashTableSize):
        hashTable.append(0)

    # print(f"len of hashTable {len(hashTable)}")

    pos = -1
    for str2hash in DuplicateStringTestData.testDataList:
        pos = pos + 1
        hashIndex = abs(hash(str2hash)) % hashTableSize
        # print(f"str[{str2hash}] hash index:[{hashIndex}]")
        hashTable[hashIndex] = hashTable[hashIndex] + 1
        if hashTable[hashIndex] == 2:
            # print(f" {str2hash} {hashTable[hashIndex]} is a duplicate")
            # Find the first occurance of the dup string
            firstPos = GetFirstOccuranceOfStr(pos,DuplicateStringTestData.testDataList)
            solutionLists.append([firstPos, pos])

        if hashTable[hashIndex] > 2:
            # print(f" {str2hash} {hashTable[hashIndex]} is another duplicate")
            slIndex = GetIndexOfSolutionListWithDupStr(pos,solutionLists, DuplicateStringTestData.testDataList)
            solutionLists[slIndex].append(pos)

    dtEnd = datetime.datetime.now()
    method_elapsed_time = dtEnd - dtStart 
    return DuplicateStringsResults("Hash", method_elapsed_time,solutionLists)

#==================================================================================================

def FindDupStrings_Set_Method(DuplicateStringTestData):
    solutionLists = []
    testDataSet = {""}

    dtStart = datetime.datetime.now()
    solutionLists.clear()

    pos = -1
    for str in DuplicateStringTestData.testDataList:
        pos = pos + 1
        setLengthBeforeAdd = len(testDataSet)
        testDataSet.add(str)
        setLengthAfterAdd = len(testDataSet)
        if setLengthBeforeAdd == setLengthAfterAdd:
            # See if the duplicate str is already in a solution list
            slIndex = GetIndexOfSolutionListWithDupStr(pos,solutionLists, DuplicateStringTestData.testDataList)
            if( slIndex >= 0):
                solutionLists[slIndex].append(pos)
            else:
                # Find the first occurance of the dup string
                firstPos = GetFirstOccuranceOfStr(pos,DuplicateStringTestData.testDataList)
                solutionLists.append([firstPos, pos])

    dtEnd = datetime.datetime.now()
    method_elapsed_time = dtEnd - dtStart 
    return DuplicateStringsResults("Set", method_elapsed_time,solutionLists)

#==================================================================================================

def FindRemainingDuplicateStrings(pos, dupStr, testDataList, slnSset):
    finds = [];
    for i in range(pos + 1, len(testDataList)):
        if (dupStr == testDataList[i]):
            if (i not in slnSset):
                finds.append(i)
    return finds


def FindDupStrings_Brute_Force_Method(DuplicateStringTestData):
    solutionLists = []
    slnList = []
    solutionSet = {""}
    dtStart = datetime.datetime.now()
    solutionLists.clear()
    solutionSet.clear()

    slnListCount = 0

    for posA in range(len(DuplicateStringTestData.testDataList)):
        if (posA not in solutionSet):
            for posB in range(posA + 1, len(DuplicateStringTestData.testDataList)):
                if (posB not in solutionSet):
                    if DuplicateStringTestData.testDataList[posA] ==  DuplicateStringTestData.testDataList[posB]:
                        # print(f"posA [{posA}] and posB [{posB}] are duplicates")
                        # Find all the dups till the end of the string
                        solutionLists.append([posA, posB])
                        solutionSet.add(posA)
                        solutionSet.add(posB)
                        dupStr = DuplicateStringTestData.testDataList[posB]
                        slnList = FindRemainingDuplicateStrings(posB, dupStr, DuplicateStringTestData.testDataList, solutionSet)
                        if (len(slnList) > 0):
                            for posC in slnList:
                                solutionLists[slnListCount].append(posC)
                                for slnPos in slnList:
                                    solutionSet.add(slnPos)
                        # print(f"solutionSet {solutionSet}")

    dtEnd = datetime.datetime.now()
    method_elapsed_time = dtEnd - dtStart 
    # print(f"solutionLists = {solutionLists}")
    return DuplicateStringsResults("Brute Force", method_elapsed_time,solutionLists)

#==================================================================================================

def FindDupStrings_MethodPassedData(funcNum, DuplicateStringTestData):
    if funcNum == 1:
        methodResults = FindDupStrings_Hash_Method(DuplicateStringTestData)

    if funcNum == 2:
        methodResults = FindDupStrings_Set_Method(DuplicateStringTestData)

    if funcNum == 3:
        methodResults = FindDupStrings_Brute_Force_Method(DuplicateStringTestData)


    # print(f"Solution Lists: {DuplicateStringTestData.solutionLists} Method Lists: {methodResults.indexList}")
    if methodResults.indexList == DuplicateStringTestData.solutionLists:
        resultStr = "PASS"
    else:
        resultStr = "FAIL"
    print(f" {resultStr}: Medthod: [{methodResults.methodName}], Test Data Name: **{DuplicateStringTestData.name}**, Elapsed Time: {methodResults.elapsed_time.total_seconds()}")
    return

#==================================================================================================
#==================================================================================================

async def main():
    print("Main start")

    # Build test data
    dupStringTestData.append(DuplicateStringTestData("No Dups", ["abcd1", "abcd2", "ABCD3"],[]))
    dupStringTestData.append(DuplicateStringTestData("One Dup Str 1", ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP01","ABCD5"],[[3, 4]]))
    dupStringTestData.append(DuplicateStringTestData("One Dup Str 2", ["abcd1", "DUP01", "abcd2", "ABCD3", "DUP01","ABCD5"],[[1, 4]]))
    dupStringTestData.append(DuplicateStringTestData("One Dup Str 3", ["DUP01", "abcd2", "abcd3", "ABCD4", "ABCD5","DUP01"],[[0, 5]]))
    dupStringTestData.append(DuplicateStringTestData("One Dup Str 4", ["DUP01", "abcd2", "DUP01", "ABCD4", "ABCD5","DUP01"],[[0, 2, 5]]))
    dupStringTestData.append(DuplicateStringTestData("Multiple Dup Str 1", ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP01","ABCD5", "DUP02", "ABCD7","DUP02"],
                                                     [[3, 4], [6,8]]))

    dupStringTestData.append(DuplicateStringTestData("Multiple Dup Strs 2", ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP02","ABCD5", "DUP01", "ABCD7","DUP02"],
                                                     [[3, 6], [4,8]]))

    dupStringTestData.append(DuplicateStringTestData("Multiple Dup Strs 3", 
        ["abcd1", "abcd2", "ABCD3", "DUP01", "DUP02","ABCD5", "DUP01", "ABCD7","DUP02","DUP01"],
                                                     [[3, 6, 9], [4,8]]))
    print()

    # Run all the test data thru all the methods.
    for i in range(1,4):
        for testData in dupStringTestData:
                FindDupStrings_MethodPassedData(i, testData)
                print()

    print()

asyncio.run(main())

