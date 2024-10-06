'''
Made By: Ethan Larson
Class: CS 101
Subject: Lab 4
Date: 9/24/24
Task: Create an algebra solver (required to create find roots for trinomial)
'''
from startUpFile import startUpClass
from findMethodsFile import findMethodsClass

#global variables
lstNums = ["0","1","2","3","4","5","6","7","8","9","."]
lstAlpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lstOper = ["+","-","^","*","/","(",")"]


startUp  = startUpClass(lstNums,lstAlpha,lstOper) #creating object

startUp.startProcess() #creates input, listifies type, checks for invalid chars
startUp.consolidateNums() #Consolidates numbers

#getters
lstInput = startUp.getFinalInput()
lstType = startUp.getFinalType()
print(lstInput)
print(lstType)

findMethods = findMethodsClass(lstInput,lstType)
findMethods.checkMethods()
findMethods.getSolutions()
