'''
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자. 출처

입력 - 화면에서 숫자로 된 문자열을 입력받는다.
"4546793"
출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
"454*67-9-3"
'''
def DashInsert(str_num):
    even_count = 0
    odd_count = 0

    for cha_num in str_num:
        start = cha_num
        if int(cha_num) % 2 == 1:
            odd_count += 1
            if even_count != 0:
                even_count = 0
            if odd_count >= 2:
                cha_num = cha_num.replace(cha_num, "-"+cha_num)
        elif int(cha_num) % 2 == 0:
            even_count += 1
            if odd_count != 0:
                odd_count = 0
            if even_count >= 2:
                cha_num = cha_num.replace(cha_num, "*"+cha_num)

        str_num = str_num.replace(start, cha_num)

    return str_num

print(DashInsert('4546793'))
