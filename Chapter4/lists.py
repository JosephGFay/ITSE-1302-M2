from utils.utils import answer, question, exercise
def lists():
    # Exercises with lists.
  # ======================================
  exercise('lists')
  
  question(1)
  # 1. Using list slicing get the sublist [4,9] and [10,23]
  l = [1,4,9,10,23]
  answer(f"{l[1:3]} and {l[3:]}")
  
  question(2)
  # 2. Apppend the value 90 to the end of the list 'l'. Check the difference between list     concatentation and the append method.
  l.append(90)
  answer(f"{str(l)}\n\t\tThe append method alters the original list variable\n\t\tby adding the appended value to the list.\n\t\tConcatenation does not alter the oringal list variable")
  
  question(3)
  # 3. Calculate the average value of all values on the list. 
  l = [1,4,9,10,23]
  answer((sum(l)) / len(l))
  
  question(4)
  # 4. Remove the sublist [4,9]
  for i in l[1:3]:
    l.remove(i)
  answer(l)
  
  