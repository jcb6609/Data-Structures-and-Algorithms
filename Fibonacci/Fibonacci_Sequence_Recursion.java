//FibonacciSequence_Recursion

public class Main{
  
  private static long fibonacci(int n){ //fibonacci method
    
    if(n <= 1){return n;} //fibonacci() method 
    
    long nthFibonacci = (fibonacci(n - 1) + fibonacci(n - 2));
    return nthFibonacci;
  }
  
  public static void main(String[] args){ //main() method
    int n = 4;
    
    System.out.println("Fibonacci sequence until f(" + n + "):");
  
    for(int i = 0; i <= n; i++){ //print fibonacci sequence until f(n)
      System.out.print(fibonacci(i) + " ");
    }
    
    System.out.println("\nRemember, the fibonacci sequence has base case f(0) = 0 and f(1) = 1;");
    System.out.println("So that, f(n) = f(n - 1) + f(n - 2) for n >= 2.");
  }}