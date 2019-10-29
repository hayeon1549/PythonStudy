def func(n):
    if n==1:
        return 1
    elif n%2==0:
        n=n//2
    else:
        n=3*n+1
    return (func(n)+1)

max_num=0
max_len=0

a,b=[int(i) for i in input("입력 : ").split()]
for n in range(a,b+1):
    len=func(n)

    if len>max_len:
        max_num=n
        max_len=len

print(max_num,max_len)