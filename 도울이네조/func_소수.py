def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
          

n=int(input("소수 판별할 정수를 입력해 주세요 : "))
print(is_prime(n))