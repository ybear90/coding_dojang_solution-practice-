nNum = int(input())

# Check if it is perfect number
def isPerfectN(num):
    cSum = 0
    for i in range(1, num):
        if num % i == 0:
            cSum += i
    if cSum == num:
        return True
    else:
        return False

perfList = []
for i in range(1,nNum+1):
    if isPerfectN(i) == True:
        perfList.append(i)

print("Result: ", perfList)
    
