import os
from colorama import init
from termcolor import colored
init()

def clear_terminal():
  os.system('clear')

def answer(string=None, let=None):
  if string != None and let == None:
    print(f'\ta. {string}')
  elif string != None and type(let) == int:
    if string!= None and let == 0:
      print(f'\ta. {string}')
    elif string != None and let > 0:
      print(f"\t   {string}")
  else:
    print(f"\t{let}. {string}")



def exercise(string):
  print(colored(f"\n# EXERCISES WITH {str(string.upper())}",'red'))

def question(num):
  print(colored(f"\nQuestion # {num}", 'blue'))

def header_red(string):
  print(colored(string, 'red'))

def header_blue(string):
  print(colored(string, 'blue'))

def header_green(string):
  print(colored(string, 'green'))

def terminal_input():
  inp = input(colored("\n@ITSE-1302-M2:-~ ", 'blue'))
  return inp

def list_files(list):
  count = 1
  for i in list:
    print(f"\t{count}. {i.__name__}.py")
    count += 1
  
  
  
