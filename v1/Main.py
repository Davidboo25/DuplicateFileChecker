import os
from collections import defaultdict
import hashlib
m_fileDict = defaultdict(list)

def getUserInput(inputFolder = None ):
    # If there was no input declared, ask the user for a folder.
    if(inputFolder == None):
        inputFolder = input("Please enter in a folder to be searched: ")
        if(os.path.isdir(inputFolder)):
            createHashs(inputFolder)
            dupeList = findDupes(m_fileDict)
            printDupes(dupeList)
        else:
            print("You have entered an invalid directory. Please try again.")
    else:
        if (os.path.isdir(inputFolder)):
            createHashs(inputFolder)
            dupeList = findDupes(m_fileDict)
            printDupes(dupeList)
        else:
            print("You have entered an invalid directory. Please try again.")
    return

def createHashs(inputPath):
    # This goes through each file in the given root dir
    # then it goes to each subdir, and then the files under that sub dir.
    # This is a weird breadth first / depth first search.
    #m_fileDict = defaultdict(list)

    for path, subdirs, files in os.walk(inputPath):
        for fileName in files:
            # Create the full path of the file using the name and relative location.
            fullPath = (os.path.join(path, fileName))

            # This reads and hashes the file contents.
            # This is in-efficient due to reading the whole file.
            # If files were large and in high numbers, this would take a long time.
            # Another solution could be hashing the first+last bit of the files.
            m_fileDict[hashlib.md5(open(fullPath, 'rb').read()).hexdigest()].append(fullPath)
    return

def findDupes(inputDict):
    dupeList = []
    for fileList in inputDict.values():
        # If the length of the list is more than one, there are duplicates of that file.
        if len(fileList) > 1:
            # Add the File list that has duplicates to a list containing every instance of duplicates.
            dupeList.append(fileList)
    return dupeList

def printDupes(inputList):
    if(not inputList):
        print("There are no duplicates in this folder and it's subfolders.")
    else:
        for listItem in inputList:
            print("These files are exactly the same: ", end="")
            for item in listItem:
                print(item + " , ",end="" )
            print("")
    return

#Release
getUserInput()





