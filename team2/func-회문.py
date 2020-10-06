#어떤 숫자를 입력했을 때 회문이 되도록 하는 재귀함수를 작성하시오.

def func(n):
    if str(n) == str(n)[::-1]:
        return n
    else:
        n+=int(str(n)[::-1])
        return func(n)

#def func(i):
#   if str(i)==str(i)[::-1]: return 0
#   return func()

a=int(input("숫자를 입력하세요 : "))
print(func(a))