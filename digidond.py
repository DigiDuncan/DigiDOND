import random
import digilogger as logger

version = "0.0.1"

cases = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None,
        7: None, 8: None, 9: None, 10: None, 11: None, 12: None,
        13: None, 14: None, 15: None, 16: None, 17: None, 18: None,
        19: None, 20: None, 21: None, 22: None, 23: None, 24: None,
        25: None, 26: None}
possiblevalues = [0.01, 1, 5, 10, 25, 50,
    75, 100, 200, 300, 400, 500, 750,
    1000, 5000, 10000, 25000, 50000, 75000,
    100000, 200000, 300000, 400000, 500000, 750000, 1000000]

currentround = 1
caseslefttochoose = 6
chosencase = 0
chosenvalue = 0

def main():
    generateCases()
    beginning()
    printCases()

def generateCases():
    global cases
    random.shuffle(possiblevalues)
    for i in range(len(possiblevalues)):
        cases[i+1] = possiblevalues[i]

def printCases():
#     [1] [2] [3] [4] [5] [6]
# [7] [8] [9] [10] [11] [12] [13]
#  [14] [15] [16] [17] [18] [19]
#[20] [21] [22] [23] [24] [25] [26]

    casestoprint = []
    stringtoprint = ""
    for casenum in range(0, len(cases) + 1):
        if cases.get(casenum) is not None:
            casestoprint.append(casenum)

    stringtoprint += "    "
    for i in range(1, 7):
        if i in casestoprint: stringtoprint += f"[{i}]"
        else: stringtoprint += f"[{' ' * len(str(i))}]"
    stringtoprint += "\n "
    for i in range(7, 14):
        if i in casestoprint: stringtoprint += f"[{i}]"
        else: stringtoprint += f"[{' ' * len(str(i))}]"
    stringtoprint += "\n  "
    for i in range(14, 20):
        if i in casestoprint: stringtoprint += f"[{i}]"
        else: stringtoprint += f"[{' ' * len(str(i))}]"
    stringtoprint += "\n"
    for i in range(20, 27):
        if i in casestoprint: stringtoprint += f"[{i}]"
        else: stringtoprint += f"[{' ' * len(str(i))}]"

    print(stringtoprint)

def beginning():
    global chosencase, chosenvalue
    print("Choose a case to make your own!")
    chosencase = int(input(">"))
    chosenvalue = cases[chosencase]
    cases[chosencase] = None
    print(f"You got ${chosenvalue}!")

def playRound(round):
    pass

#Run the main loop.
main()
