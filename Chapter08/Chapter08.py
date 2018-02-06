def Answer8_3():
    print('(a):')
    print(list(range(10)))
    print('(b):')
    print(list(range(3,19,3)))
    print('(c):')
    print(list(range(-20, 861,220)))

def isprime(x):
    count = x//2
    while count > 1:
        if (x % count) == 0:
            return False
        count -= 1
    else:
        return True


def Answer8_4():
    for x in range(3,100):
        if isprime(x):
            print('%d is prime' % x)
        else :
            pass


if __name__ == '__main__':
    print('the answer of 8_3 is:')
    Answer8_3()
    print('\nthe answer of 8_4 is:')
    Answer8_4()
