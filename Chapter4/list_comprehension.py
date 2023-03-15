from utils.utils import answer, question, exercise
def list_comprehension():
  
  # Exercises with lists comprehensions.
  exercise('list comprehension')
  
  question(1)
  # 1. Using list comprehension, create a list with squares of the first 10 numbers.
  x = [x**2 for x in range(10)]
  answer(x)
  
  question(2)
  # 2.Using list comprehension, create a list with the cubes of the first 20 numbers.
  x = [x**3 for x in range(20)]
  answer(x)
  
  question(3)
  # 3. Create a list comprehension with all even numbers from 0 to 20, and another with all odd numbers.
  even = [x for x in range(20) if x % 2 == 0]
  odd = [x for x in range(20) if x % 2 == 1]
  answer(f"even: {even}",'a')
  answer(f"odd: {odd}", 'b')
  
  question(4)
  # 4. Create a list of squares of even numbers from 0 to 20, and sum the list using the 'sum' function. The result should be 1140. First create the list using list comprehensions, check the result, then apply the sum to the list comprehension.
  even = [x**2 for x in range(20) if x % 2 == 0]
  answer(sum(even))
  
  question(5)
  # 5. Make a list comprehension that returns a list with the squares of all even numbers from 0 to 20, but ignore those numbers that are divisible by 3. In other words, each number should be divisible by 2 and not divisible by 3.
  even = [x**2 for x in range(20) if x % 2 == 0 and not x % 3 == 0]
  answer(even)
  
  
  
  
  