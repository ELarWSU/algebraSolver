'''
Made by: Ethan Larson
Class: CS101
Subject: Lab 4
Date: 10/04/24
Task: Asks the user for what they want to solve, generates a list of character types for each input character, and then consolidates numerical values
'''


#Class to check for invalid characters, consolidate number char, and manipulates list for looping
class startUpClass:

    #Constructor Method that retrieves input and type
    def __init__(self,num,alp,opr):
        self.num = num
        self.alp = alp
        self.opr = opr
        self.lsInput = []
        self.lsType = []

    def createInput(self):
        lstInput = []
        strInput = input("Please enter something to solve: ") #Creates input
        strInput = strInput.lower() #lowers all alpha chars
        for x in range(0,len(strInput)): #Breaks down the input into an array
            lstInput.append(strInput[x:x+1])
        return lstInput

    def listifyType(self,lstInput):
        lstType = []
        for x in lstInput:
            blnExitNumSuccess = False
            blnExitNumFail = False
            blnExitAlphaSuccess = False
            blnExitAlphaFail = False
            blnExitOperSuccess = False
            blnExitOperFail = False
            intCountNum = 0
            intCountAlpha = 0
            intCountOper = 0
            intLenNum = len(self.num)
            intLenAlpha = len(self.alp)
            intLenOper = len(self.opr)
            while blnExitNumSuccess == False and intCountNum <= intLenNum and blnExitNumFail == False: #runs until the loop is told to quit or there are no numbers left
                try: #if x is a number it compares
                    if x == self.num[intCountNum]: #sees if x was a valid number
                        lstType.append("num")
                        blnExitNumSuccess = True
                    else:
                        intCountNum = intCountNum + 1
                except: # x wasn't a number, it was either a letter or an operand or other
                    blnExitNumFail = True

            while blnExitAlphaSuccess == False and intCountAlpha <= intLenAlpha and blnExitNumFail == True and blnExitAlphaFail == False:
                try:
                    if x == self.alp[intCountAlpha]:
                        lstType.append("alp")
                        blnExitAlphaSuccess = True
                    else:
                        intCountAlpha = intCountAlpha + 1
                except:
                    blnExitAlphaFail = True
            
            while blnExitOperSuccess == False and intCountOper <= intLenOper and blnExitAlphaFail == True and blnExitOperFail == False:
                try:
                    if x == self.opr[intCountOper]:
                        lstType.append("opr")
                        blnExitOperSuccess = True
                    else:
                        intCountOper = intCountOper + 1
                except:
                    lstType.append("inv")
                    blnExitOperFail = True
                    
        return lstType

    #This function checks to see if an invalid character has been entered
    def startProcess(self):
        blnExit = False
        while blnExit == False:
            self.lsInput = self.createInput()
            self.lsType = self.listifyType(self.lsInput)
            blnInv = False
            for x in self.lsType:
                if x == "inv":
                    blnInv = True

            if blnInv == False:
                blnExit = True

    def consolidateNums(self):
        intCount = 0 #index for comparing next item
        blnExit = False #boolean condition for loop
        lenStart = len(self.lsType) - 1 #starting length of types list - 1 because the length of a string doesn't count 0
        self.lsType.append("stp") #appends extra list so doesn't run into error when comparing the next type

        while blnExit == False and intCount < lenStart:
            if self.lsType[intCount] == "stp": #if the loop # = extra type then exit the loop
                blnExit = True
            elif self.lsType[intCount] == "num" and self.lsType[intCount + 1] == "num": #if the current loop number
                self.lsInput[intCount] = self.lsInput[intCount] + self.lsInput[intCount + 1] #Adds the next number to the pre-existing number
                del self.lsInput[intCount + 1] #deletes next input item
                del self.lsType[intCount + 1] #deletes next type item
            else:
                intCount = intCount + 1 #if nothing is found add another loop iteration


    def getFinalInput(self):
        return self.lsInput
    
    def getFinalType(self):
        return self.lsType
        