#Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
#If it is the case we will return k, if not return -1.

import math
def dig_pow(n,p):
    results = []
    for digit in map(int, str(n)):
        operation = digit ** p
        p +=1
        results.append(operation)
    sum_all = sum(results)
    k = sum_all//n
    if sum_all == n * k:
        return k
    else:
        return -1
   

print(dig_pow(46288, 3))
            