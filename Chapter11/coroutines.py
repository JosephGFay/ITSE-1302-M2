from utils.utils import answer, question, exercise

def coroutines():
  
  exercise('coroutines')

  #1 Create a coroutine named 'square' that prints the square of any sent value
  question(1)

  def square():
    while True:
      val = yield
      answer(f'send({val}): {val**2}')

  sq = square()
  next(sq)
  sq.send(10)

  #2 Implement the minimize coroutine that keeps and prints the minimum value that is sent to the function
  question(2)

  def minimize():
    init = True
    while True:
      if init:
        init = False
        min = yield
        answer(f"send({min}): {min}")

      val = yield

      if val < min:
        min = val

      print(f"\t   send({val}): {min}", end='\n  ')

  min = minimize()
  next(min)
  min.send(5)
  min.send(7)
  min.send(1)
  min.send(0)
