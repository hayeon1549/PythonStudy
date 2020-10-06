number=int(input("숫자를 입력해주세요 (1~1000):"))

while True:

    predict=int(input("예상 숫자를 입력해주세요 (1~1000):"))

    if number>predict:
        print("UP이다 뀨")
    elif number<predict:
        print("DOWN이다 뀨")
    else:
        print("정답이다 뀨쀼뀨쀼뀨쀼뀨쀼뀨쀼뀨쀼뀨쀼")
        break