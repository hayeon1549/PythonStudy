check=[2,3,4,5,6,7,8,9,2,3,4,5]
number=[]
sum=0

user=input("주민번호를 숫자만 입력하세요>>")

for i in range(len(user)):
    number.append(int(user[i]))

for i in range(len(check)):
    sum+=number[i]*check[i]

sum=(11-sum%11)%10

if sum!=number[-1]:
    print("잘못된 주민번호입니다.")
elif number[6]%2 == 0:
    print("여성의 주민번호입니다.")
else:
    print("남성의 주민번호입니다.")