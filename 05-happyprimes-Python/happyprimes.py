# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def ishappyprimenumber(n):
    # Your code goes here
    if(isprime(n)):
        if(ishappynumber(n)):
            return True
        return False


def isprime(n):
    i = 1
    count = 0
    while(i <= n):
        if(n%i == 0):
            count += 1
        i += 1
    if(count <= 2):
        return True
    return False

def ishappynumber(n):
    rem = sum = 0
    if(n == 1):
        return True
    while(n > 0):
        rem = n%10
        sum += rem*rem
        n //= 10
    res = sum
    if(res != 1 and res != 4):
        res = ishappynumber(res)
    if(res == 1):
        return True
    else:
        return False

print(ishappynumber(1418854))
# print(ishappyprimenumber(14832))