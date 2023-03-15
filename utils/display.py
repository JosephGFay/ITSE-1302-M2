from Chapter3.numbers import numbers as Chapter3_numbers
from Chapter3.strings import strings as Chapter3_strings
from Chapter4.lists import lists as Chapter4_lists
from Chapter4.list_comprehension import list_comprehension as Chapter4_list_comp
from Chapter5.math_module import math_module as Chapter5_math_module
from Chapter5.functions import functions as Chapter5_functions
from Chapter5.recursion import recursion as Chapter5_recursion
from Chapter6.for_loop import for_loop  as Chapter6_for_loop
from Chapter6.while_loop import while_loop as Chapter6_while_loop
from Chapter7.dictionaries import dictionaries as Chapter7_dictionaries
from Chapter7.sub_dictionaries import sub_dictionaries as Chapter7_sub_dictionaries
from Chapter8.classes import classes as Chapter8_classes
from Chapter8.inheritance import inheritance as Chapter8_inheritance
from Chapter9.iterators import iterators as Chapter9_iterators
from Chapter10.generators import generators as Chapter10_generators
from Chapter11.coroutines import coroutines as Chapter11_coroutines
from Chapter11.pipelines import pipelines as Chapter11_pipelines
import utils.utils as utils
from colorama import init
from termcolor import colored
init()

def directory_list():
  running = True
  while running:
    utils.clear_terminal()
    print("ITSE-1302-M2 Course Directory")
    print("Author: Joseph Fay\n")
    print(colored("Select a Chapter to view exercises \n", 'blue'))
    for i in range(3,13):
      print(f"{i}. <DIR> Chapter{i}")
      
    print(colored('\nEnter a single digit value corresponding to chapter number:', 'light_yellow'))
    
    inp = input(colored("\n@ITSE-1302-M2:-~ ", 'blue'))
  
    utils.clear_terminal()
      
    if inp == '3':
      exercise_list([Chapter3_numbers, Chapter3_strings])
    elif inp == '4':
      exercise_list([Chapter4_lists, Chapter4_list_comp])
    elif inp == '5':
      exercise_list([Chapter5_math_module, Chapter5_functions, Chapter5_recursion])
    elif inp == '6':
      exercise_list([Chapter6_for_loop, Chapter6_while_loop])
    elif inp == '7':
      exercise_list([Chapter7_dictionaries,Chapter7_sub_dictionaries])
    elif inp == '8':
      exercise_list([Chapter8_classes,Chapter8_inheritance])
    elif inp == '9':
      exercise_list([Chapter9_iterators])
    elif inp == '10':
      exercise_list([Chapter10_generators])
    elif inp == '11':
      exercise_list([Chapter11_coroutines,Chapter11_pipelines])
    elif inp == '12':
      print("Not implemented yet")
    else:
      print("ERROR: Invalid Input. Please Enter a corresponding single digit value")
  
  
def exercise_list(exes):
  running = True
  while running:
    utils.clear_terminal()
    utils.header_blue("Select the exercise file to view: ")
    utils.list_files(exes)
    utils.header_red("\nType Q to return to menu")
    
    while True:
      inp = utils.terminal_input()

      if inp == 'q' or inp == 'Q':
        running = False
        break
      
      try:
        inp = int(inp)
  
        if inp > len(exes) + 1:
          print(
            "ERROR: Invalid Input. Please enter a valid exercise number\n"
          )
        else:
          utils.clear_terminal()
          exes[int(inp)-1]()
          break
          
      except:
        print(inp)
        print("ERROR: Invalid Input. Please enter a valid integer value.\n")

    while True and running:
      utils.header_red("\nType Q to return to menu")
      utils.header_green("\nWould you like to view another exercise? Y/N")
      inp = input(">")
      if inp == 'y' or inp =='Y':
        break
      elif inp == 'n' or inp == 'N' or 'q' or 'Q':
        running = False
        break
      else:
          print("Please enter 'Y' or 'N'")
        