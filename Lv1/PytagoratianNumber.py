'''
세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
예를 들면 3^2 + 4^2 = 9 + 16 = 25 = 5^2 이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
'''

# Sol 1) brutal search
for i in range(100, 1000):
   for j in range(i + 1, 1000):
       for k in range(j + 1,1000):
           if i < j and j < k:
               if (i + j + k) == 1000:
                   if (i**2 + j**2) == k**2:
                       print('i, j, k: ', i, j, k)
                       print('i * j * k: ', i * j * k)

# Sol 2) By using mathematical algorithm
# a = m^2 - n^2, b = 2mn c = m^2 + n^2(m > n)
for m in range(2, 1000):
    for n in range(1, 1000):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        
        if (a + b + c == 1000) and \
           (a**2 + b**2  == c**2):
            if (a > 0 and b > 0) and c > 0:
                print("a, b, c: ", a, b, c)
                print("a * b * c: ", a * b * c)
