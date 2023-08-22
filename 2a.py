def Fibo(n):
    ft = 0
    st = 1
    tt = 0

    if n <= 0:
        print("The value of N is expected to be greater than 0 but received", n)
    else:
        print("The", n, "terms of the Fibonacci series are:")
        print(ft)
        print(st)

        n -= 2

        while n > 0:
            tt = ft + st
            print(tt)
            ft = st
            st = tt
            n -= 1

n = int(input("Enter the value of n: "))
Fibo(n)
