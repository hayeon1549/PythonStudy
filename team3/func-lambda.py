d=[lambda a,b:a+b,lambda a,b:a-b,lambda a,b:a*b,lambda a,b:a/b]
a,b,c=[int(i) for i in input("더하기는 0 뺴기는 1 나누기는 2 곱하기는 3 나머지는 4\n계산할 숫자 2개와 연산자를 숫자로 입력해주세요 (ex:1 2 2)").split()]
print("계산 결과 : {}".format(d[c](a,b)))