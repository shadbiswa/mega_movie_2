#funtions go here 

#checks that ticket name is not blank 
def not_blank(question):
   valid = False 
  
   while not valid:
     response = input(question)
#if name is not blank, program continues
     if response != "":
       return response
       #if name is blank, show error(& repeat loop)
     else:
       print("sorry - this cant be blank, " "please enter your name")


# funtion goes here

def int_check(question):

  error = "please enter a whole number between {} "
  
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
        
#************* main routine ******

#set up dictionaries / lists needed to hold data 

#ask user if they used the program before & show instructions if necessary 

#loop to get ticket deatils 
       
       
#initialise loop so that it runs at least once 
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    if count < 4:
     print("You have {} seats" " left".format(MAX_TICKETS - count))
  
#warns user that only one seat is left!
    else:
     print("*** there is one seat left!! ***")


#get details..
 #get name (cant be blank)
    name = not_blank("name: ")

  # end loop if the exit codde is entered
    if name == "xxx":
      break 

#get age (between 12 and 130)
    age = int_check("age: ")

  # check that age is valid
    if age < 12:
      print("sorry you are too young for this movie")
      continue
    elif age > 130:
      print("that is very old -it looks like a mistake")
      continue

    count += 1

# end of ticket loop

if count == MAX_TICKETS:
  print("you have sold all the available tickets!")
else:
  print("you have sold {} tickets. \n"
       "there are {} places still available".format(count, MAX_TICKETS - count))


  #calculate ticket price 

  #loop to ask for snacks

  #calculate snack price

  # ask for payment method (and apply surcharge if necesary)

#calculate total sales and profit

#output data to text file 
