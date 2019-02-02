"""
Duplicate Numbers
일전에 뭐 게임 회사에서 본 간단한 퀴즈 테스트 입니다.

0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.

sample inputs: 0123456789 01234 01234567890 6789012345 012322456789

sample outputs: true false false true false
"""
r_input = input().split()

def inputInit(cList):
    for i in range(10):
        cList[i] = 0

def DuplicateNumbers(lList):
    # Initialize check input list
    check_value = list()
    for i in range(len(lList)):
        check_value.append(True)

    check_input = list()
    for i in range(10):
        check_input.append(0)

    # Checking duplicate number
    for i in range(len(lList)):
        for j in range(len(lList[i])):
            check_input[int(lList[i][j])] += 1

        # Finally check duplicate number(T or F)
        for k in range(len(check_input)):
            print(check_input[k])
            if check_input[k] != 1:
                check_value[i] = False

        inputInit(check_input)

    print(check_value)

DuplicateNumbers(r_input)
