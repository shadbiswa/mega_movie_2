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

  #get name (cant be blank)
  name = not_blank("name: ")

  #get age (between 12 and 130)

  #calculate ticket price 

  #loop to ask for snacks

  #calculate snack price

  # ask for payment method (and apply surcharge if necesary)

#calculate total sales and profit

#output data to text file 
