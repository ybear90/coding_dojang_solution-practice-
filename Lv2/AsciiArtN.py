"""
Write a program that lets the user enter in an odd positive integer (you may assume the input is always valid), and prints out an ASCII art letter N made using the character N.

If the input is 1, the output is:

N
If the input is 3, the output is:

N N
NNN
N N
If the input is 5, the output is:

N   N
NN  N
N N N
N  NN
N   N
If the input is 7, the output is:

N     N
NN    N
N N   N
N  N  N
N   N N
N    NN
N     N
The pattern continues on like this. The output may contain trailing spaces.
"""
input_number = int(input())

for i in range(input_number):
    for j in range(input_number):
        if (j == 0) or (j == input_number-1):
            print("N", end='')
        elif (j > 0) and (j < input_number-1):
            if i == j:
                print("N", end='')
            else:
                print(" ", end='')
    print()
