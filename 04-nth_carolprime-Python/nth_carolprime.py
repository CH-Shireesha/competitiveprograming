# Write the function nthCarolPrime(n), which takes a non-negative int and returns the nth Carol Prime, 
# which is a prime number of the form ((2**k - 1)**2 - 2) for some value positive int k. For example, 
# if k equals 3, ((2**3 - 1)**2 -2) equals 47, which is prime, and so 47 is a Carol Prime. 
# The first several Carol primes are: 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527,... As such, 
# nthCarolPrime(0) returns 7.
# Note: You must use a reasonably efficient approach that quickly works up to n==9, which 
# will return a 12-digit answer! In particular, this means you cannot just edit isPrime. 
# Hint: you may need to generate only Carol numbers, and then test those as you go 
# for primality (and you may need to think about that hint for a while for it to make sense!).


def fun_nth_carolprime(n):
    num = 1
    i = 0
    while(i <= n):
        res = 0
        res = (2**num)-1
        res = (res*res -2)
        if(isprime(res)):
            i += 1
        num += 1
    return (res)

def isprime(n):
    c = 0
    i = 1
    while(i <= n):
        if(n%i == 0):
            c += 1
            if(c > 2):
                break
        i += 1
    if(c == 2):
        return True
    else:
        return False

print(fun_nth_carolprime(3))