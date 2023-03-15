from utils.utils import answer, question, exercise

def recursion():
  # Exercises with recursive functions.
  exercise('recursive functions')
  
  #1 Implement the factorial function and test it with several different values. Cross-check with a calculator.
  question(1)
  
  def factorial(x):
    if x == 0:
      return 1
    else:
      return x * factorial(x-1)
  
  print("\ta.", end=" ")
  print(factorial(9))
  
  #2 Implement a recursive function to compute the sum of the (n) first integer numbers (where (n) is a function parameter). Start by thinking about the base case (the sum of the first 0 integers is?) and then think about the recursive case.
  question(2)
  
  def recursive_sum(n):
    if n == 0:
      return 0
    else:
      return n + recursive_sum(n-1)
      
      
  print("\ta.", end=" ")
  print(f"Result of recursive sum function(5): {recursive_sum(5)}")
  
  #3 The Fibonnaci sequence is a sequence of numbers in which each number of the sequence matches the sum of the previous two terms. Given the following recusive definition implement. (fib(b))
  question(3)
  
  def fib(n):
    if n == 0 or n == 1:
      return n
    else:
      return fib(n-1) + fib(n-2)
  
  print("\ta.", end=" ")
  # for i in range(12):
  #   print(fib(i), end=", ")
  for i in range(12):
    print(fib(i), end=", ")