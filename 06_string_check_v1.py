#string checking functions, takes in 

#question and list of valid response


def string_checker(question, to_check):

  valid = False
  while not valid:

    response = input(question).lower()

    if response in to_check:
      return response 

    else:
      for item in to_check:
        #checks if response is the first letter of an item 
        if response == item[0]:
          #note: returns the entire response 
          #rather than just the first letter
          return item 

    print("sorry that is not valid response")

# *** Main Routine starts here ***

