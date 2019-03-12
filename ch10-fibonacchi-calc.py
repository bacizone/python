import time

def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacchi(n-1) + (n-2)

for i in range (20, 955, 5):
    start = time.time()
    result = fibonacchi(i)
    end = time.time()
    duration = end - start
    print(i, result, duration)