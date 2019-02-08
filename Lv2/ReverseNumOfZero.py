"""
N!의 정의는 다음과 같습니다.

N! = 1 * 2 * 3 * 4 ... N
이때 N!를 정수로 변환 해 뒤에서 부터 연속되는 0의 갯수를 구하세요.

예) f(12) -> 2 # 12!은 479001600 f(25) -> 6 # 25!은 15511210043330985984000000

출처: codewars
"""
def f(num):
    factori = 1
    i = factori

    while i <= num:
        factori *= i
        i += 1
        
    return factori

numFact = int(input("Enter the factorial number: "))
numZero = 0

for s in str(f(numFact)):
    if s == '0':
        numZero += 1

print("f(%d) -> %d" % (numFact, numZero))
