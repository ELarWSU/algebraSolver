'''
Made By: Ethan Larson
Class: CS 101
Subject: Lab 4
Date: 9/24/24
'''

#global variables
lstNums = ["0","1","2","3","4","5","6","7","8","9","."]
lstAlpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lstOper = ["+","-","^","*","/","(",")"]
intLenNum = len(lstNums)
intLenAlpha = len(lstAlpha)
intLenOper = len(lstOper)


#Gather's input and creates a list from input
def startInput():
    lstInput = []
    strInput = input("Please enter the the trinomial: ") #Creates input
    strInput = strInput.lower() #lowers all alpha chars
    for x in range(0,len(strInput)): #Breaks down the input into an array
        lstInput.append(strInput[x:x+1])
    return lstInput

#Runs input function and assigns a list
lstInput = startInput()

#Creates type list from which determines what are numbers, operands, and alphabet chars
def listifyType(lstInput):
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

        while blnExitNumSuccess == False and intCountNum <= intLenNum and blnExitNumFail == False: #runs until the loop is told to quit or there are no numbers left
            try: #if x is a number it compares
                if x == lstNums[intCountNum]: #sees if x was a valid number
                    lstType.append("num")
                    blnExitNumSuccess = True
                else:
                    intCountNum = intCountNum + 1
            except: # x wasn't a number, it was either a letter or an operand or other
                blnExitNumFail = True

        while blnExitAlphaSuccess == False and intCountAlpha <= intLenAlpha and blnExitNumFail == True and blnExitAlphaFail == False:
            try:
                if x == lstAlpha[intCountAlpha]:
                    lstType.append("alp")
                    blnExitAlphaSuccess = True
                else:
                    intCountAlpha = intCountAlpha + 1
            except:
                blnExitAlphaFail = True
        
        while blnExitOperSuccess == False and intCountOper <= intLenOper and blnExitAlphaFail == True and blnExitOperFail == False:
            try:
                if x == lstOper[intCountOper]:
                    lstType.append("opr")
                    blnExitOperSuccess = True
                else:
                    intCountOper = intCountOper + 1
            except:
                lstType.append("inv")
                blnExitOperFail = True

    return lstType

#Runs list function and assigns a new list
lstType = listifyType(lstInput)

#Class to check for invalid characters, consolidate number char, and manipulates list for looping
class validChar:

    #Constructor Method that retrieves input and type
    def __init__(self,input,type):
        self.input = input
        self.type = type

    #This function checks to see if an invalid character has been entered
    def check(self):
        intCount = 0
        self.type.append("stp")
        intLen = len(self.type)
        while intCount < intLen:
            if self.type[intCount] == "inv":
                self.input = startInput() #reruns input function
                self.type = listifyType(self.input) #reruns list type
                intCount = 0
            else:
                intCount = intCount + 1
        try:
            self.type.remove("stp")
        except:
            pass #removes from listing if found

    def conNums(self):
        intCount = 0
        self.type.append("stp")
        lenCount = len(self.type)
        blnExit = False
        while blnExit == False:
            if self.type[intCount] == "stp":
                blnExit = True
            elif self.type[intCount] == "num" and self.type[intCount + 1] == "num":
                self.input[intCount] = self.input[intCount] + self.input[intCount + 1]
                del self.input[intCount + 1]
                del self.type[intCount + 1]
            else:
                intCount = intCount + 1

validChar1  = validChar(lstInput,lstType) #creating object
validChar1.check() #run function that checks for invalid chars, if so, reruns
validChar1.conNums() #Consolidates numbers
lstInput = validChar1.input #reassign input list
lstType = validChar1.type #reassign type list

#Class to find computation methods for the user
class compute:

    intValidMethods = 0
    strMethods = ""

    def __init__(self,input,type):
        self.input = input
        self.type = type

    def checkMethods(self):
        intCount = 0
        blnExit = False
        blnBasicMath = True
        #Checks to see if it can do basic math
        while intCount < len(self.type) and blnExit == False:
            if self.type[intCount] == "alp":
                blnBasicMath = False
                blnExit = True

            else:
                intCount = intCount + 1
        
        if blnBasicMath == True:
            self.strMethods = ("- Basic Math\n")
            self.intValidMethods = self.intValidMethods + 1


        #Solve for x


    def askUser(self):
        print(self.strMethods)
            


compute1 = compute(lstInput,lstType)#Creates object
compute1.checkMethods() #Runs check method to determine what avaiable methods they're to solve for problems
compute1.askUser()
lstInput = compute1.input #Reassigns input list (if needed)
lstType = compute1.type #Reassigns type list (if needed)

#Prints finalized list
print(lstInput)
print(lstType)


            