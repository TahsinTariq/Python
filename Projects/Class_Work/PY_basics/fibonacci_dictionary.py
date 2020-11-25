from functools import reduce

if __name__ == '__main__':
    n = 10
    fib = lambda n: [n, reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]]
    factorial = lambda n:reduce(lambda x,n:x*n, range(1, n+1),1)
    print(factorial(4))
    # print(dict(fib(i) for i in range(n+1)))