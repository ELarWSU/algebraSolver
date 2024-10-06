''''
Made By: Ethan Larson
Class: CS 101
Subject: Lab 4
Date: 10/05/24
Task: Using the user's input, this class retrieves all the avaiable methods that can be used
'''

class getMethodsClass:
    
    def __init__(self, lsInput, lsType):
        self.lsInput = lsInput
        self.lsType = lsType
    
    def checkBasicArithmetic(self):
        for x in self.lsType:
            if x == "alp":
                return False
            if x == "stp":
                return True