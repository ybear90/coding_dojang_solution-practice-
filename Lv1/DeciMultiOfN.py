'''
어떤 수 x가 주어졌을때 조건에 따라 x가 n의 배수인지 판별하는 코드를 작성하라.
x는 0 이상의 정수이며 조건에 맞지 않는 입력은 주어지지 않는다.
여기서 하나의 함수인지 여러 함수인지는 본인이 선택하면 된다.
단 절대 산술연산자 중 %와 /는 코드에 없도록 한다.
그리고 divmod() 함수를 쓰는것도 금지한다
코드를 짧고 창의적으로 하는 것을 목적으로 한다. 속도는 크게 중점을 두지 않는다.
n의 종류는 2,3,5,7,11,13이다.
원하는 n만 선택해서 풀 수도 있다.
'''

# trial number setting.
trial = int(input("Number of inputs? : "))

# Memory list setting.
natural_list = list()
prime_list = list()
loop_count = trial

# Saving data to memory lists.
while loop_count > 0:
    natural, prime = input().split()
    loop_count -= 1
    natural_list.append(int(natural))
    prime_list.append(int(prime))

# Out the results
print("\nThe results are as follow: ")
for i in range(trial):
    is_correct = 0
    is_true = False
    while natural_list[i] > is_correct:
        is_correct += prime_list[i]
        if natural_list[i] == is_correct:
            is_true = True
    if is_true == True:
        print(1)
    else:
        print(0)
