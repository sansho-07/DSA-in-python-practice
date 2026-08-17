def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

x = int(input("Enter a number to print a fibonacci series: "))

if x<=0:
    print("Enter a values greater than 0")

else:
    print(f"Fibonacci series of {x} ")
    for i in range(x):
        print(fibo(i), end = " ")