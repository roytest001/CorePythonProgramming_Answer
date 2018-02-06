import math

def Answer5_8():
    (edge, radius) = eval(input("Enter two num use the edge, radius style: "))
    print("the area of square is %d\t and cube is %d" % (edge**2 ,6 * (edge**2)))
    print("the volume of cube is %d" % edge**3)
    print("the area of round is %d\t and ball is %d" % (math.pi * (radius**2) ,4 * math.pi * (radius**2)))
    print("the volume of ball is %d" % (4/3 * math.pi *(radius**3)))

def Answer5_11():
    print("(a):")
    for num in range(20):
        if num % 2 == 0:
            print(num)
    print("(b):")
    for num in range(20):
        if num % 2 != 0:
            print(num)
    print("(c):")
    print("the simple method is watch the mode of div by 2")
    print("(d):")
    (num,den) = eval(input("Enter two nums(use the style like this: num, den):"))
    if (num % den) == 0:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    Answer5_8()
    Answer5_11()