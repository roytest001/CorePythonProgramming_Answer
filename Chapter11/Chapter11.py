def Answer11_2(x, y):
    return (x + y, x * y)

def Answer11_6(stringIn, *args):
    print(stringIn, 'the len of string is ', len(stringIn))
    

if __name__ == "__main__":
    print("\nthe answer of 11_2 is:")
    print("x + y = %d, x * y = %d" % (Answer11_2(3, 10)))
    print("\nthe answer of 10_6 is:")
    Answer11_6("Python3 is cool!")