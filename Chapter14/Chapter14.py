def Answer14_1():
    """
    Callable object:
    functions, methods, class, callable class instances
    The difference between exec and eval:
    the exec is to exe the command in string and the eval is to calculate the value of a string expression
    """

def Answer14_2():
    """
    The difference between input() and raw_input():
    raw_input() returns user input as a string; input() return the 
    evaluation of the user input as a Python expression. In other words:
      input() == eval(raw_input())
    """


if __name__ == "__main__":
    print("\nthe answer of 14_1 is:")
    print(Answer14_1.__doc__)
    print("\nthe answer of 14_2 is:")
    print(Answer14_2.__doc__)