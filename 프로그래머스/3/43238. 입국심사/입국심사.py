def solution(n, times):

    a, b = 0, 1
    while not is_ok(n, times, b):
        a, b = b, b*2
        

    while a<b:
        m = (a+b) // 2
        if is_ok(n, times, m):
            a, b = a, m
        else:
            a, b = m+1, b
    


    return a
def is_ok(n, times, x):
    return n <= sum(x//i for i in times)