from utils.utils import answer, question, exercise

def dictionaries():
  
  exercise('dictionaries')
  
  ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
  }
  
  #1 How many students are in the dictionary?
  question(1)
  answer(len(ages))
  
  #2 Implement a function recieves the "ages" dictionary as parameters and returns the average age of the students. Use the 'items' method.
  question(2)
  
  def average_age(dict):
    values = []
    for key, value in dict.items():
      values.append(value)
  
    return (sum(values) / len(values))
  
  
  answer(average_age(ages))
  
  #3 Implement a function that recieves the 'age' dictionary as parameters and returns the name of the oldest student.
  question(3)
  
  
  def oldest_student(dict):
    oldest_age = 0
    for student, age in dict.items():
      if age > oldest_age:
        oldest_age = age
        oldest_student = student
  
    return oldest_student
  
  
  answer(f"The oldest student is: {oldest_student(ages)}")
  
  #4 Implement a function that recieves the 'ages' dictionary and a number 'n' and returns a new dict where each student is (n) year older. For Instance, new_ages(age, 10) returns a copy of 'ages' where each student is 10 years older.
  question(4)
  
  
  def new_ages(dict, n):
    new_dict = {}
    for student, age in dict.items():
      new_dict.update({student: age * n})
    return new_dict
  
  
  answer(f"{new_ages(ages, 10)}")
