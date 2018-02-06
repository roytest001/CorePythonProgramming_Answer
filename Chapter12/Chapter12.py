def Answer12_2():
    """
    (a):
    the first is import mymodule               ==> mymodule.foo()
    the seconde is: from mymodule import foo   ==> foo()

    (b):
    use the first way, then the module name is brought into the local namespace
    use the second way, the the foo() is brought into the local namespace 
    """

if __name__ == "__main__":
    print("\nthe answer of 12_2 is:")
    print(Answer12_2.__doc__)