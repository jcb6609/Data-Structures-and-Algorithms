//Fibonacci_Sequence_Memoization

public class Main{
  
  private static long[] fibonacciArray; //fibonacciArray (special variable) declaration
  
  private static long fibonacci(int n){
    if (n <= 1){return n;} //base case
    
    //Java int and long arrays automatically initialize all elements to 0 when created.
    if(fibonacciArray[n] != 0){return fibonacciArray[n];} //recusion stopper/ saver check
    
    long nthFibonacci = (fibonacci(n - 1) + fibonacci(n - 2));
    fibonacciArray[n] = nthFibonacci; //fibonacciArray filling 
    return nthFibonacci;
  }
  
  public static void main(String[] args){
    int n = 4;
    
    //array creation
    fibonacciArray = new long[n + 1]; //Size n+1 accommodates index 0, matching the Fibonacci sequence's start at f(0) = 0 
    
    System.out.println("Fibonacci sequence until f(" + n + "):");
    
    for(int i = 0; i <= n; i++){
      System.out.print(fibonacci(i) + " ");
    }
    
    System.out.println("\nRemember, the fibonacci sequence has base case f(0) = 0 and f(1) = 1;");
    System.out.println("So that, f(n) = f(n - 1) + f(n - 2) for n >= 2.");
  }}