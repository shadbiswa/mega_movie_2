# funtion goes here

def int_check(question, low_num, high_num):

  error = "please enter a whole number between {} " \
          "and {}".format(low_num, high_num)
  
  valid = False
  while not valid:

    #ask user for number and check if it valid
      try:
          response = int(input(question))

          if response <= 0:
              print(error)
          else:
              return response 

    #if an integer is not entered, display an error
      except ValueError:
        print(error)
      

#main routine goes here
age = int_check("age: ", 12, 130)
