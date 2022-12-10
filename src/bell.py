from functools import cache

@cache
def stirling(n , k):
    if (n == k):
        return 1
    elif (k == 0 or n == 0 or n < k):
        return 0
    return stirling(n-1, k-1) + k*stirling(n-1,k) 

def bell():
    cur = 0
    while True:
        _sum = 0
        for it in range(cur+1):
            _sum += stirling(cur, it)
        yield _sum
        cur += 1

if __name__ == '__main__':
    bell_gen = bell()
    print(type(bell_gen))
    result = [next(bell_gen) for _ in range(20)]
    print(result)