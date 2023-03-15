from utils.utils import answer, question, exercise


def strings():
  # EXERCISES WITH STRINGS
  exercise('strings')

  #1 Initialize the string "abc" on a variable "s":
  question(1)
  s = "abc"

  # a. Use function to get the length of the string.
  answer(f"The Length of 's': {len(s)}", 'a')

  # b. Write the neccesary sequence of operations to transform the string "abc" in "aaabbbccc".
  answer(f"{s[0]*3 + s[1]*3 + s[2]*3}", 'b')

  #2 Initalize the sting "aaabbbccc" on a variable named "s":
  question(2)
  s = "aaabbbccc"

  # a. Use a funcion that allows you to find the first occurence of "b" in the string, and the first occurence of "ccc"
  answer(f"The first occurence of 'b' in {s} is: {s.index('b')}")
  answer(f"The first occurence of 'ccc' in {s} is: {s.index('ccc')}")
  # b. Use a function that allows you to replace all occurences of "a" to "X", and then use the same function to change only the first occurence of "a" to "X"
  answer(f"Replacing 'a' with 'X' in {s}: {s.replace('a', 'X')}", 'b')
  answer(
    f"Replacing first occurence of 'a' with 'X' in {s}: {s.replace('a', 'X', 1)}",
    'b')

  #3 Starting from the string "aaa bbb ccc", what sequences of operations do you need to arrive at the following string? You can use the "replace" function.
  question(3)
  s = "aaa bbb ccc"
  # a. "AAA BBB CCC"
  s = s.upper()
  answer(s, 'a')
  # b. "AAA bbb CCC"
  answer(s.replace('BBB', 'bbb'), 'b')
