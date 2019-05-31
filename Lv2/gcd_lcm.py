'''
3개 이상의 여러 가지의 수가 주어졌을 때, 공약수, 최대공약수를 찾는 알고리즘을 구하시오.

6015240, 1507968, 4530816

의 공약수, 최대공약수, 최소공배수를 구하시오.
'''

# 유클리드 호제법을 사용하여 푼다
# 최대공약수 함수
def gcd(big_num, small_num):
    big_num, small_num = max(big_num, small_num), min(big_num, small_num)
    while small_num:
        big_num, small_num = small_num, (big_num % small_num)
    
    return big_num
    
# 최소공배수 함수
def lcm(big_num, small_num):
    return (big_num * small_num) / gcd(big_num, small_num)

# 공약수 찾는 함수
def find_com_divisor(num):
    div_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            div_list.append(i)
    
    return div_list

# 리스트의 원소를 곱하는 함수
def multiply(arr):
    return eval('*'.join([str(n) for n in arr]))

# 세 수의 리스트
num_list = [6015240, 1507968, 4530816]
length_list = len(num_list)

# 세 수의 공약수 구하기
com_divisors_list = []

# 1) 공약수의 리스트 구하기
for i in range(length_list):
    for j in range(i + 1, length_list):
        com_divisors_list.append(find_com_divisor(gcd(num_list[i], num_list[j])))

# 2) 구한 리스트에서 하나의 공약수 집합을 추리기
set_com_divisors = set()
for i in range(len(com_divisors_list)):
    for j in range(i + 1, len(com_divisors_list)):
        if len(set_com_divisors) == 0:
            set_com_divisors = set(com_divisors_list[i]) & set(com_divisors_list[j])
        else:
            set_com_divisors = set_com_divisors & (set(com_divisors_list[i]) & set(com_divisors_list[j]))

print("com_divisors_list: ", com_divisors_list)
print("공배수의 집합: ", set_com_divisors)

# 최대공약수 구하기
print("최대공약수: ", max(set_com_divisors))

# 최소공배수 구하기
print("최소공배수 ", int(multiply(num_list) / (max(set_com_divisors) ** (length_list - 1))))
