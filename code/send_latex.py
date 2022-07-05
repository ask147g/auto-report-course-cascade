import string

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


def sendLatexC2(column:int, x1:float, x2:float, data:float):
    try:
        file = open(fileName, "a")
        file.write(str(column))
        file.write(";")
        file.write(reDot(x1))
        file.write(";")
        file.write(reDot(x2))
        file.write(";")
        file.write(reDot(data))
        file.write("\n")
    except:
        print("ERROR WHILE WRITE TO FILE")


def preSendLatex(name:string):
    try:
        file = open(name, "w")
        file.write("avar;value\n")
        file.close()
    except:
        print("ERROR WHILE OPEN FILE")


def preSendLatexC2(name:string):
    try:
        file = open(name, "w")
        file.write("avar;x1;x2;value\n")
        file.close()
    except:
        print("ERROR WHILE OPEN FILE")


def setName(name:string):
    global fileName
    fileName = name