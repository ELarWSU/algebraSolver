'''
Made By: Ethan Larson
Class: CS 101
Subject: Lab 4
Date: 10/05/24
Task: This class tries finding all the computational methods of solving mathmatical problems. This could be arthemetic, algebra, and more.
        Once the method(S) are found, it asks the user for what method it wants to use to solve their problem.
'''

from getMethodsFile import getMethodsClass
from solutionsFile import solutionsClass

class findMethodsClass:
    
    lstMethods = [] #creates empty array

    def __init__(self,lsInput,lsType):
        self.lsInput = lsInput
        self.lsType = lsType
        self.getMethods = getMethodsClass(self.lsInput,self.lsType) #Creates getMethods instance
        self.solutions = solutionsClass(self.lsInput,self.lsType) #Creates solutions instance

    def checkMethods(self):
        blnBasicArithmetic = self.getMethods.checkBasicArithmetic()
        if blnBasicArithmetic == True:
            self.lstMethods.append("Basic Arithmetic")
        
        if blnBasicArithmetic == False:
            print("Basic is false")




    def getSolutions(self):
        #Prints found methods
        print("\nPlease enter the number for the problem you're trying to solve")
        print("---------------------------------------------------------------")
        for x in range(0,len(self.lstMethods)):
            print(str(x + 1) + ". " + self.lstMethods[x])


        strInput = input("\nEnter Number Here: ")
        intInput = int(strInput)

        for x in range(0,len(self.lstMethods)):
            if x == intInput - 1:
                pass
                #run the method/algorithm