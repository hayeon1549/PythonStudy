for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print("")
print("-----------------------")

for i in range(5)[::-1]:
    for j in range(5):
        if j<i:
            print(end=" ")
        else:
            print("*",end="")
    print("")
