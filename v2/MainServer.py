import os
from collections import defaultdict
import hashlib
import ipaddress
import socket

m_fileDict = defaultdict(list)

def mainRunner(inputFolder = None ):
    outputText = ""
    # If there was no input declared, ask the user for a folder.
    if (inputFolder == None):
        inputFolder = input("Please enter in a folder to be searched: ")
        if (os.path.isdir(inputFolder)):
            createHashs(inputFolder)
            dupeList = findDupes(m_fileDict)
            outputText = printDupes(dupeList)
            # Return the collected display data to the client
            return outputText
        else:
            return ("You have entered an invalid directory. Please try again.")
    else:
        if (os.path.isdir(inputFolder)):
            createHashs(inputFolder)
            dupeList = findDupes(m_fileDict)
            outputText = printDupes(dupeList)
            # Return the collected display data to the client
            return outputText
        else:
            return ("You have entered an invalid directory. Please try again.")
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
    outputText = "\n"
    for listItem in inputList:
        outputText += ("These files are exactly the same: ")
        for item in listItem:
            outputText += (item + " , " )
        outputText += ("\n")
    return outputText

# Local host
TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

while True:
    outputText = ""
    data = conn.recv(BUFFER_SIZE)
    # Decode the data to receive the string.
    data = data.decode()

    # If there is no data, break out and close the connection.
    if not data:
        break
    else:
        # If there is data sent to the server, get the files for that folder.
        outputText = mainRunner(data)

    conn.send(outputText.encode())
conn.close()