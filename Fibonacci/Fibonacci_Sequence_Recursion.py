def main():
    x = int(input("Select an x value for the fibonacci function f(x): "))
    
    # range() handles int i = 0 automatically -> range(0, ...) = range(...) where 0 is set by default (no need to set unless any change needed, such as i = 1 --> range(1, ...))
    # i <= 5 --> range(5 + 1) = range(6) or i <= n --> range(n + 1)
    # i++ (post-increment operator, which adds 1 to the value of a variable) is also set by default in the third argument for range(..., ..., 1), so that no change is needed unless requiring to modify the increment/decrement default set 
    for i in range(0, x + 1, 1): # range(start, stop, step)
        print(fibonacci(i), end=' ') # default for print is end='\n'
    

def fibonacci(n):
    if(n <= 1):
        return n
    
    nthFibonacci = (fibonacci(n - 1) + fibonacci(n - 2))
    return nthFibonacci


main()