al=set("green")
b1=set("apple")
c=list(al|b1)
c.sort()
grape=list()
for i in range(5):
    a=int(input("숫자 한 개 : "))
    grape+=c[a]
print(grape)
