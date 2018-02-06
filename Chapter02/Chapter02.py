def Answer05():
    "this is the answer of 2-5"
    count = 0
    print("use the 'while loop'")
    while count < 11:
        print(count)
        count += 1
    print("use the 'for loop'")
    for count in range(11):
        print(count)


def Answer06(x):
    "this is the answer of 2-6"
    if x > 0:
        print("x is positive")
    elif x == 0:
        print("x is zero")
    else :
        print("x is negative")


def Answer07(strIn):
    "this is the answer of 2-7"
    print("use the 'while loop':")
    strIndex = 0
    strLen = len(strIn)
    while strIndex < strLen:
        print(strIn[strIndex], end = '')
        strIndex += 1
    print("")    
    print("use the 'for loop':")
    for eachStr in strIn:
        print(eachStr, end = '')
    print("")    


def Answer08(fiveElement):
    "this is the answer of 2-8"
    print("use the 'while loop':")
    elementLen = len(fiveElement)
    elementIndex = 0
    sum = 0
    while elementIndex < elementLen:
        sum += fiveElement[elementIndex]
        elementIndex += 1    
    print("the sum is ",sum)
    sum = 0
    print("use the 'for loop':")
    for eachElement in fiveElement:
        sum += eachElement
    print("the sum is ", sum)


if __name__ == '__main__':
    print("the answer of 2-5 is:")
    Answer05()
    print("the answer of 2-6 is:")
    x = input("Enter a inter to judge:")
    Answer06(int(x))
    print("the answer of 2-7 is:")
    strIn = input("Enter a string to print:")
    Answer07(strIn)
    print("the answer of 2-8 is:")
    fiveElement = input("Enter a list or tuple of five elements to do the sum:")
    Answer08(eval(fiveElement))
    print("the type of input is",type(eval(fiveElement)))

    