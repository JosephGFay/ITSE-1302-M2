from utils.utils import answer, question, exercise

def while_loop():
  exercise('while loop')
  #1 Implement a function that recieves a number as parameter and prints, in decreasing order, which numbers are even and which are odd, untill it reaches 0.
  question(1)  
  
  def even_odd(n):
    while n > 0:
      print(f"{'Even' if n % 2 == 0 else 'Odd'} number: {n}", end="\n\t   ")
      n -= 1
  
  
  print("\ta.", end=" ")
  
  even_odd(10)
  