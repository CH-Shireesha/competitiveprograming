# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

primes = []
def fun_nth_smithnumber(n):
    j = 1
    while(j < n):
        if (isSmith(j)):
            print(j)
        i = i+1
    return j

def isSmith(j):
    num = j
    sum = 0
    i = 0
    while(primes[i] <= j/2):
        while(j%primes[i] == 0):
            p = primes[i]
            j = j/p
            while(p > 0):
                sum += (p%10)
                p //= 10
        i = i+1
    if(not j == 1 and not j == num):
        while(j > 0):
            sum += num%10
            num //= 10
    sumd = 0
    while(j > 0):
        sumd += num%10
        num //= 10
    return (sum == sumd)


print(isSmith(4))
print(fun_nth_smithnumber(1))