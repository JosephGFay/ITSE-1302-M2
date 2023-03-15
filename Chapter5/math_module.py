from utils.utils import answer, question, exercise
import math

def math_module():
  
  exercise('math module')
  
  #1 Find the greatest common divisor of the following pairs of numbers:
  #  (15,21), (152,200), (1988,9765).
  question(1)
  
  pairs = [[15,21], [152,200], [1988,9765]]
  i = 0
  for nums in pairs:
    answer(math.gcd(nums[0], nums[1]), chr(97+i))
    i += 1
    
  #2 Compute the base-2 logarithm of the following numbers: 0,1,2,6,9,15.
  question(2)
  
  numbers = [0,1,2,6,9,15]
  i = 0
  for num in numbers:
    try:
      # print(math.log2(num), end="\n\t\t")
      answer(math.log2(num), chr(97+i))
    except:
      # print("  ValueError", end="\n\t\t")
      answer('ValueError', chr(97+i))
    i += 1
  
  #3 Use the "input" function to ask the user for a number and show the result of the sine, cosine, and tangent of the number. Make sure that you convert the user input from string to a number.
  question(3)
  
  user_input = int(input("Enter a numerical value: "))
  print(f"\ta.  Sine: {math.sin(user_input)}\n\t\tCosine: {math.cos(user_input)}\n\t\tTangent: {math.tan(user_input)}")

  

  