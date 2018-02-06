
def Answer13_2():
    """
    The difference between functions and methods:
    Methods are basically functions but tied to a specific class object type. 
    They are defined as part of a class and are executed as part of an instance of that class
    """

def Answer13_5():
    """
    Delegation:
    It makes no difference whether we use open() or capOpen() to read our file 
    because in capOpen.py, we delegated all of the reading functionality to the 
    Python system defaults, meaning that no special action is ever taken on reads.
    The same code would be executed, i.e., none of read(), readline(), or readlines()
    are overrdden with any special functionality.
    """


if __name__ == "__main__":
    print("\nthe answer of 13_2 is:")
    print(Answer13_2.__doc__)
    print("\nthe answer of 13_5 is:")
    print(Answer13_5.__doc__)