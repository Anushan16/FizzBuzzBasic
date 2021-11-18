
def FizzBuzz():

  endInterger = int(input("What interger did you want to run the FizzBuzz sequence until? "))

  for e in range(1,endInterger):

    if e % 3 == 0 and e % 5 == 0:
      print("FizzBuzz")
    elif e % 3 == 0:
      print("Fizz")
    elif e % 5 == 0:
      print("Buzz")
    else:
      print (e)



FizzBuzz()