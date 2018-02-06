def Answer7_1():
    """
    dict.update can merge two dict together
    """

def Answer7_3():
    print("(a):")
    stuDict = {'name':'zhu', 'number':220151257, 'age':27, 'sex':'man'}
    keys = list(stuDict.keys())
    keys.sort()
    print("the keys in dict is:")
    for eachNum in keys:
        print(eachNum,'\t',end = '')
    print("\n(b):")
    for eachNum in keys:
        print('key = %s    value = %s' %(eachNum, stuDict[eachNum]))

def Answer7_4():
    keyList = [1,2,3,4]
    valList = ['abc','def','ghi','jkl']
    dict1 = dict(list(zip(keyList, valList)))
    print('the dict is:',dict1)
    
def Answer7_7():
    dictOrg = {1:'a',2:'b',3:'c',4:'d'}
    dictRever = dict(zip(list(dictOrg.values()), list(dictOrg.keys())))
    print('the orgin of dict is:', dictOrg)
    print('the reverse of dict is:', dictRever)


if __name__ == '__main__':
    print('the answer of 7_1 is:')
    print(Answer7_1.__doc__)
    print('\nthe answer of 7_3 is:')
    Answer7_3()
    print('\nthe answer of 7_4 is:')
    Answer7_4()
    print('\nthe answer of 7_7 is:')
    Answer7_7()

