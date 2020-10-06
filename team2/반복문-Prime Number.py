for i in range(2, 100):
    cnt = 0
    for j in range(2, i):
        if i%j == 0:
            cnt += 1
    if cnt == 0:
        print(i,end=" ")

print()

for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i, end=" ")