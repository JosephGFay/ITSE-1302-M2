from utils.utils import answer, question, exercise

def sub_dictionaries():
  
  exercise('sub dictionaries')
  
  students = {
    "Peter" : {"age" : 10, "address" : "lisbon"},
    "Isabel" : {"age" : 11, "address" : "Sesimbra"},
    "Anna" : {"age" : 9, "address" : "lisbon"},
  }
  
  #1 How many students are in the students dict. Use the appropriate function.
  question(1)
  answer(f"There are {len(students)} students")
  
  
  #2 Implement a function that recieves the students dict and returns the average age.
  question(2)
  def average_age(dict):
    avg = 0
    for i in dict.values():
      avg += i['age']
  
    return avg / len(students)
  answer(f"The result of average_age(students): {average_age(students)}")
  
  
  #3 Implement a function that recieves the students dict and an address and returns a list with names of all students whose address matches the address in the arguements. For Instance, invoking "find_students(students, "Lisbon") should return Peter and Anna.
  question(3)
  def find_students(dict, address):
    found = []
    for student, info in students.items():
      if info["address"] == address:
        found.append(student)
    return found
    
  answer(f"The result of find_students(students,'lisbon'): {find_students(students, 'lisbon')}")
      
    