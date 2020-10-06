def func(n):
    print(n,end=" ")
    if n%2!=0:n=3*n+1
    else:n=n//2
    if n != 1:func(n)
    else:print(n)
n=int(input("입력 : "))
func(n)