# function to import variables to data-files
# used to read them in latex-projects

import string

firstSendLatex = False
fileName = "variables.csv"

def reDot(data:float):
    return str(data).replace('.', ',')

def sendLatex(name:string, data:float):
    try:
        file = open(fileName, "a")
        file.write(name)
        file.write(";")
        file.write(reDot(data))
        file.write("\n")
    except:
        print("ERROR WHILE WRITE TO FILE")

def preSendLatex():
    try:
        file = open(fileName, "w")
        file.write("avar;value\n")
        file.close()
    except:
        print("ERROR WHILE OPEN FILE")
