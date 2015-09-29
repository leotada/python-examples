#!/bin/env python3
#Author: https://github.com/JohnWillker

def removeWhitespaceInfile(file):
    var_file = open(file, "r")
    tmp = var_file.read()
    conc = tmp.split()
    conte = ""
    for x in range(0,len(conc)):
        conte = conte+conc[x]
    var_file.close()
    var_file = open(file, "w")
    var_file.write(conte)
    var_file.close()

file = input("Insert file's name: ")
removeWhitespaceInfile(file)
print("OK")
