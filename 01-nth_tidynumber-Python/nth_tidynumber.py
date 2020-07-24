# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    num = 1
    i = 0
    l = []
    while(i < n):
        if(istidy(num)):
            i += 1
            l.append(num)
        num += 1
    print(l)
    return num


def istidy(num):
    prev = 10
    while(num):
        rem = num%10
        num //= 10
        if(rem > prev): 
            return False
        prev = rem
    return True

print(istidy(2800))
print(fun_nth_tidynumber(499))