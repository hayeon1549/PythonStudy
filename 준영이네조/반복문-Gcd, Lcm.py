a=int(input())
b=int(input())
c=a*b

if a<b:
    a, b = b, a

while b != 0:
    a, b = b, a % b
gcd=a
lcm=c//gcd

print(gcd,lcm)