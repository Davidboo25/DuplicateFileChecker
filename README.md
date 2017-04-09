# DuplicateFileChecker
Includes two versions of duplicate file checkers when given an input folder.

## Version 1
Version 1 is a basic duplicate file checker. 
When given a folder from user input, the program will search through every file in the given folder and its subfolders for duplicates.

To run: python Main.py

## Version 2
Version 2 supports a client - server configuration of the Duplicate File Checker.
MainServer holds all of the functionality of the version 1 duplicate filer checker. It then returns the output to the client.

MainClient asks the user for an input folder and then passes that location to the server. It then displays the returned data to the user.

To run:
1. Open up one cmd and run: python MainServer.py
2. Open up a second cmd and run: python MainClient.py

