list=[1,[[3],2],[4,[5,6]],7,[8],[9,[[10]]]]

def func(li):
    sum=0
    for i in li:
        if type(i) == int: sum+=i
        else: sum+=func(i)
    return sum

print(func(list))