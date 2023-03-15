from utils.utils import answer, question, exercise
def functions():
  # Exercises with functions
  exercise('functions')
  
  #1 Implement the 'add2' function that recieves two numbers as arguements and returns the sum of the numbers. Then implement 'add3' function that recieves and sums 3 parameters.
  question(1)
    
  def add2(x,y):
    return x + y
    
  def add3(x,y,z):
    return x + y + z
    
  print("\ta.", end=" ")
  print(add2(2,4), end=", ")
  print(add3(2,4,6))
  
  #2 Implement a function that returns the greatest of two numbers given as parameters. Use the 'if' statement to compare both numbers.
  question(2)
  
  def greatest_num(x,y):
    return x if x > y else y
    
  print("\ta.", end=" ")
  print(greatest_num(5,10))
  
  #3 Implement a function named 'is_divisible' that recieves two parameters 'a and b' and returns true if 'a' can be divided by 'b' or false otherwise. A number is divisible by another when the remainder of the division is zero.
  question(3)
  
  def is_divisible(a,b):
    return True if a % b == 0 else False
    
  print("\ta.", end=" ")
  print(is_divisible(6, 2))
  
  #4 Create a function named "average" that computes the average value of a list passed as parameter to the function. Use sum and len functions.
  question(4)
  
  def average(nums):
    return sum(nums) / len(nums)
  
  print("\ta.", end=" ")
  print(average([2,4,6]))