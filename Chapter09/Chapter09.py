import sys


def Answer9_2():
    f = open('test','w')
    for x in range(10):
        f.write(str(x))
        f.write('\n')
    f.close()

    numLines = eval(input('Enter the number of line to display(num < 10): '))
    f = open('test','r')
    for eachLine in f:
        print(eachLine, end = '')
        numLines -= 1
        if numLines == 0:
            break
    f.close()

def Answer9_13():
    print("# of args", len(sys.argv))
    print("args:", sys.argv)

if __name__ == '__main__':
    print("the answer of 9_2 is:")
    Answer9_2()
    print("\nthe answer of 9_13 is:")
    Answer9_13()

