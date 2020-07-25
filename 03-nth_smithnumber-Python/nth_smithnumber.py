# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

import math

def fun_nth_smithnumber(n):
    j = 1
    c = 0
    while(c <= n):
        if (isSmith(j) and not isPrime(j)):
            c += 1
        j += 1
    return (j-1)

def isPrime(n):
    i = 1
    c = 0
    while(i <= n):
        if(n%i == 0):
            c += 1
            if(c > 2):
                break
        i += 1
    if(c == 2):
        return True
    return False

def isSmith(j):
    if(digitsum(j) == sumoffactors(j)):
        return True
    return False

def sumoffactors(n):
    l = []
    while(n%2 == 0 and n > 0):
        l.append(int(2))
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i == 0):
            l.append(int(i))
            n = n/i
    if n > 2:
        l.append(int(n))
    num = 0
    # print(l)
    for j in l:
        if(len(str(j)) == 1):
            num += j
            # print(num)
        elif(len(str(j)) > 1 and j is not n):
            # print(j, num)
            num += digitsum(j)
    # print(num)
    return num

def digitsum(n):
    sum = 0
    while(n > 0):
        rem = n%10
        sum += rem
        n //= 10
    return sum

# print(isSmith(4))
# print(fun_nth_smithnumber(1))