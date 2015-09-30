#!/bin/env python3
#Author: https://github.com/JohnWillker

def removeWhitespaceInfile(file):
    var_file = open(file, "r")
    txt = var_file.read()
    txt = txt.replace(' ', '').replace('\n', '')
    var_file.close()
    var_file = open(file, "w")
    var_file.write(txt)
    var_file.close()

file = input("Insert file's name: ")
removeWhitespaceInfile(file)
print("OK")
