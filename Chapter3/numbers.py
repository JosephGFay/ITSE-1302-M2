from utils.utils import answer, question, exercise


def numbers():
  # EXERCISES WITH NUMBERS
  exercise('numbers')

  #1 Try the following mathematical calculations and guess what is happening:
  #  ((3 / 2)), ((3 // 2)), ((3 % 2)), ((3**2))
  question(1)

  answer(f"'3 / 2'  Divides the number 3 by 2 resulting in: {3/2}", 'a')
  answer(
    f"'3 // 2' Divides the number 3 by 2 using floor division rounding to nearest integer value resulting in: {3//2}",
    'b')
  answer(
    f"'3 % 2'  Uses Modulous operator to return the remainder resulting in: {3 % 2}",
    'c')
  answer(f"'3**2' \tRaises 3 to the power of 2 resulting in: {3**2}", 'd')

  #2 Calculate the average of the following sequences of numbers:
  #  (2,4), (4,8,9), (12, 14/6, 15)
  question(2)

  def average(seq):
    i = 0
    for nums in seq:
      answer(f"Average of {nums} = {sum(nums) / len(nums)}", chr(97 + i))
      i += 1

  average([[2, 4], [4, 8, 9], [12, 14 / 6, 15]])

  #3 The volume of a sphere is given by (4/3 * pi * r^3) Calculate the volume of a sphere of radius 5.
  question(3)
  pi = 3.1415
  r = 5
  answer(f"The volume of the a sphere with a radius of 5: {4 / 3 * pi * r**3}")

  #4 Use the modulo operator (%) to check which of the following numbers is even or odd: (1, 5, 20, 60/7)
  question(4)

  def even_or_odd(nums):
    # Handler function to evalute if number is odd or even and print to terminal
    i = 0
    for num in nums:
      answer(f'The value of {num} is: {"odd" if (num % 2) else "even"}',
             chr(97 + i))
      i += 1

  even_or_odd([1, 5, 20, (60 / 7)])

  #5 Find some values for (x) and (y) such that (x < 1/3 < y) on the REPL
  question(5)
  x = .1
  y = 1
  answer(f"x({x}) < 1/3 < y({y}) = {x < 1 / 3 < y}")
