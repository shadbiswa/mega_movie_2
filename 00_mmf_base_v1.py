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
    print("You have {} seats"
       "left".format(MAX_TICKETS - count))
  
#warns user that only one seat is left!
    else:
    print("*** there is one seat left!! ***")


#get details..
 #get name (cant be blank)
    name = not_blank("name: ")
    count += 1
    print()

if count == MAX_TICKETS:
  print("you have sold all the available tickets!")
else:
  print("you have sold {} tickets. \n"
       "there are {} places still available".format(count, MAX_TICKETS - count))


  #get age (between 12 and 130)

  #calculate ticket price 

  #loop to ask for snacks

  #calculate snack price

  # ask for payment method (and apply surcharge if necesary)

#calculate total sales and profit

#output data to text file 
