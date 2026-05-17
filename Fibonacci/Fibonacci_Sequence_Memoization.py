def main():
    # variables inside functions are assumed to be local by default
    global fibonacciList # tell Python that main() has to use the global variable

    x = int(input("Select an x value for the fibonacci function f(x):"))
    fibonacciList = [0] * (x + 1) # fibonacciList creation (creates a list of size n + 1 filled with 0s automatically)
    for i in range(0, x + 1, 1):
        print(fibonacci(i), end=' ')

fibonacciList = []  # global fibonacciList declaration 

def fibonacci(n):
    if(n <= 1):
        return n
    
    if(fibonacciList[n] != 0): # recursion stopper/recursion checker
        return fibonacciList[n]
    
    nthFibonacci = (fibonacci(n - 1) + fibonacci(n - 2))
    fibonacciList[n] = nthFibonacci # soring the list
    return nthFibonacci

main()