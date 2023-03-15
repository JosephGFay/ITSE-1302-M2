from utils.utils import answer, question, exercise

def for_loop():
  
  exercise('for loop')
  
  #1 Create a function 'add' that recieves a list as parameter and returns the sum of all elements in the list. Use the 'for' loop to iterate over the elements of the list.
  question(1)
  
  def add(list):
    sum = 0
    for i in list:
      sum += i
    return sum
    
  answer(f"The result of add([5,10,15]): {add([5,10,15])}")
  
  
  #2 Create a function that recieves a list as parameter and returns the maximum value in the list. As you iterate over the list you may want to keep the maximum value found so far in order to keep comparing it with the next elements of the list.
  question(2)
  
  def maximum(list):
    max = 0
    for i in list:
      if i > max:
        max = i
    return max
    
  answer(f"The maximum value in [0,2,5,1,4,100,23,96] is: {maximum([0,2,5,1,4,100,23,96])}")
  
  
  #3 Modify the previous function such that it returns a list with the first element being the maximum value and the second being the index of the maximum value in the list. Besides keeping the maximum value found so far, you also need to keep the position where it occured.
  question(3)  
  def maximum(list):
    max = 0
    index = 0
    for i in list:
      if i > max:
        max = i
        index = list.index(i)
    return [max, index]
    
  answer(f"Maximum value and index in [0,2,5,1,4,100,23,96] is: {maximum([0,2,5,1,4,100,23,96])}")
  
  
  #4 Implement a function that returns the reverse of a list recieved as a parameter. You may create an empty list and keep adding the values in reversed order as they come.
  question(4)  
  def reverse_list(list):
    x = []
    for i in range(len(list),0, -1):
      x.append(i)
    return x
    
  answer(f"[1,2,3,4] Reversed is : {reverse_list([1,2,3,4])}")
  
  #5 Make the function 'is_sorted' that recieves a list as parameter and returns True if the list is sorted in ascending order. For instance [1,2,2,3] is ordered while [1,2,3,2] is not.
  question(5)
  
  def is_sorted(list):
    for i in range(len(list) - 1):
      if list[i] > list[i+1]:
        return False
      else:
        sorted = True
        
    return sorted
  
  answer(f"[1,2,4,3] is ascending sorted: {is_sorted([1,2,4,3])}", 'a')
  answer(f"[1,2,2,3] is ascending sorted: {is_sorted([1,2,2,3])}", 'b')
  
  #6 Implement the function 'is_sorted_dec' which is similar to the previous one but all items must be sorted by decreasing order.
  question(6)  
  def is_sorted(list):
    for i in range(len(list) - 1):
      if list[i] < list[i+1]:
        return False
      else:
        sorted = True
        
    return sorted
    
  answer(f"[3,4,2,1] is descending sorted: {is_sorted([3,4,2,1])}", 'a')
  answer(f"[3,2,2,1] is descending sorted: {is_sorted([3,2,2,1])}", 'b')
  
  #7 Implement the 'has_duplicates' function which verifies if a list has duplicated values. You may have to use two 'for' loops where each value you have to check for duplicates on the rest of the list.
  question(7)
  
  def has_duplicates(list):
  
    for i in range(len(list)):
      for j in range(1, len(list)):
        if list[i] == list[j]:
          return True
      return False
    
  answer(f"[1,2,3,4] has duplicates: {has_duplicates([1,2,3,4])}", 'a')
  answer(f"[1,2,3,1] has duplicates: {has_duplicates([1,2,3,1])}", 'b')
