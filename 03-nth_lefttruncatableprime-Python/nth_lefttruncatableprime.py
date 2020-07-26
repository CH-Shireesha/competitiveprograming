# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def fun_nth_lefttruncatableprime(n):
    num = 1
    c = 0
    while(c <= n):
        if(isprime(num)):
            l = []
            temp = num
            while(temp > 0):
                rem = temp%10
                l.append(rem)
                temp //= 10
            l = l[::-1]
            if i not in l:
                result = i
                x = i
                for j in range(len(l)):
                    result = result + l[j]*(10**(len(l)-j-1))
                    if(isprime(num-result)):
                        x += 1
                    else:
                        break
                if(x == len(l)-1):
                    c += 1
        num += 1

    return (num-1)

def isprime(n):
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