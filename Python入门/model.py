def printLine(char, times):
    print(char*times)


def printLines(char, times):
    row = 0
    while row < 5:
        printLine(char, times)
        row += 1


printLines("-", 50)
name = "Tom"
