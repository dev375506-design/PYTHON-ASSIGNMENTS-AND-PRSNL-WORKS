def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci series up to 200:")
i = 0
while True:
    val = fib(i)
    if val > 200:
        break
    print(val, end=" ")
    i += 1