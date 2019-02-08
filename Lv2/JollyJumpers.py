"""
출처 : programming-challenges.com

n개의 정수(n>0)로 이루어진 수열에 대해 서로 인접해 있는 두 수의 차가 1에서 n-1까지의 값을 모두 가지면 그 수열을 유쾌한 점퍼(jolly jumper)라고 부른다. 예를 들어 다음과 같은 수열에서

1 4 2 3
앞 뒤에 있는 숫자 차의 절대 값이 각각 3,2,1이므로 이 수열은 유쾌한 점퍼가 된다. 어떤 수열이 유쾌한 점퍼인지 판단할 수 있는 프로그램을 작성하라.

Input

각 줄 맨 앞에는 3000 이하의 정수가 있으며 그 뒤에는 수열을 나타내는 n개의 정수가 입력된다. 맨 앞 숫자가 0이면 출력하고 종료한다.

output

입력된 각 줄에 대해 "Jolly" 또는 "Not Jolly"를 한 줄씩 출력한다

Sample Input

4 1 4 2 3
5 1 4 2 -1 6
※ 주의: 각 줄의 맨 앞의 숫자는 수열의 갯수이다. 첫번째 입력인 4 1 4 2 3 의 맨 앞의 4는 뒤에 4개의 숫자가 온다는 것을 의미함

Sample Output

Jolly
Not jolly
"""
def JollyMachine():
    while True:
        input_list = list(map(int,input().split()))
        # Check if input_number list's length is correct
        # Exception error processing
        numElem = len(input_list) - 1
        out_number = (numElem != input_list[0])
        out_range = (input_list[0] > 3000 or input_list[0] < 0)
        exit_condition = (input_list[0] == 0)

        if out_number or out_range:
            print("Error!")
        elif exit_condition:
            print(input_list)
            print("The program is ended.")
            break
        # print(input_list)

        # Check this progression is Jolly or Not Jolly
        cmp = len(set(list(range(1,numElem))) - set([abs(input_list[i] - input_list[i+1])
                                                     for i in range(1, numElem)]))

        if cmp == 0:
            print("Jolly")
        else:
            print("Not Jolly")
            
JollyMachine()
