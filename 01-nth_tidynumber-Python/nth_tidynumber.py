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
    while(i <= n):
        prev = 10
        while(num):
            rem = num%10
            num //= 10
            if(rem > prev): 
                break
            prev = rem
        l.append(num)
        num += num
    return l

    return 0