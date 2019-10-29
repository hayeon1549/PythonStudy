from functools import reduce  #reduce 함수를 사용하기 위해서는 꼭 해줘야함!!!!!

# map, reduce를 사용하여 줄임말을 만드세요

char=reduce(lambda a, b:a+b,list(map(lambda a:a[0],"내년 자율동아리 브레인스티밍 참여하고 싶으면 준영이에게".split(' '))))

print(char)