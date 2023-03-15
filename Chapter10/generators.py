from utils.utils import answer, question, exercise

def generators():
  
  exercise('generators')
  #1 Implement a generator called 'squares' to yield the square of all numbers from (a) to (b) Test it with a for loop and print each of the yielded values.
  question(1)
  
  def squares(a, b):
    while a < b:
      yield a
      a += 1
  
  results = [x for x in squares(0,10)]
  answer(f"squares(0,10): {results}")
      
  #2 Create a generator to yield all the even numbers from 1 to (n)
  question(2)
  
  def even(n):
    i = 1
    while i < n:
      if i % 2 == 0:
        yield i
      i += 1
  
  results = [x for x in even(10)]
  answer(f"even(10): {results}")
  
  #3 Create another generator to yield all the odd numbers from 1 to (n)
  question(3)
  
  def odd(n):
    i = 1
    while i < n:
      if i % 2 == 1:
        yield i
      i += 1
  
  results = [x for x in odd(10)]
  answer(f"odd(10): {results}")
  
  #4 Implement a generator that returns all numbers from (n) down to 0
  question(4)
  
  def descend(n):
    while n > 0:
      yield n
      n -= 1
      
  results = [x for x in descend(10)]
  answer(f"descend(10): {results}")
  
  #5 Create a generator to return the fibonnaci sequence startin from the first element up to (n).
  question(5)
  
  def fibonacci(n):
    i = 0
    first = 0
    second = 1
    while i < n:
      if i == 0 or i == 1:
        yield i
      else:
        value = first + second
        first = second
        second = value
        yield value
      i += 1
        
  results = [x for x in fibonacci(12)]
  answer(f"fibonacci(12): {results}")
  
  #6 Implement a generator that returns all consecutive pairs of numbers from 0 to (n). (0,1), (1,2), (2,3)
  question(6)
  
  def pairs(n):
    i = 0
    while i < n:
      yield (i, i+1)
      i += 1
  
  results = [x for x in pairs(5)]
  answer(f"pairs(5): {results}")