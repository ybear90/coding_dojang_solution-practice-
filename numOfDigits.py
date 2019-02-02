"""
1~1000에서 각 숫자의 개수 구하기
예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자

10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5

그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개
"""

# Initialization
start = 1
end = 1000
digits = dict()

for i in range(10):
    digits[i] = 0
    
for x in range(start, end+1):
    for a in str(x):
        digits[int(a)] += 1

print(digits)
