'''
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

If it is the case we will return k, if not return -1.

'''

def dig_pow(n, p):
    sum = 0
    for dig in str(n):
        dig = int(dig)
        sum = sum + pow(dig,p)
        p += 1
    if (sum % n == 0):
        print(sum)
        # print(sum//n)
        return sum//n
    else:
        return -1

dig_pow(46288,3)