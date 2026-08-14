def main():
    fib_num = int(input("n = "))
    result = fibonacci(fib_num)
    print(f"f({fib_num}) = {result}")


# Recursive approach
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n >= 2):
        return (fibonacci(n - 1) + fibonacci(n - 2))


main()