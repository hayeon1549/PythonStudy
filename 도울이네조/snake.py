m=[]
for i in range(10):
    m.append([])
    for j in range(10):
        m[i].append(0)

for i in range(10):
    a=input().split()
    for j in range(10):
        m[i][j]=int(a[j])

i=1
j=1
m[1][1] = 9
while m[8][8]!=9:
    m[i][j] = 9

    if m[i][j+1] == 0:
        j += 1
    else:
        i += 1

for i in range(10):
    for j in range(10):
        print(m[i][j],end=' ')
    print()