def sumEven(alist):
    sum = 0
    for i in alist:
        sum += i
    if sum%2 == 0:
        return True
    else:
        return False
list = [-3, 8, 5, -10, -5]
print(sumEven(list))
