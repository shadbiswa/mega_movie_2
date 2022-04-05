profit = 0

name = ""
while name != "xxx":

  name = input("Name: ") # replace with funtion call 
  if name == "xxx":
    break

  age = int(input("age: ")) # replace with funtion 

  if age < 16:
    ticket_price = 7.5
  elif age < 65:
    ticket_price = 10.5
  else:
    ticket_price = 6.5 

  profit_made = ticket_price - 5
  profit += profit_made

  print("{} : ${:.2f}".format(name, ticket_price)) 

print("profit from tickets: ${:.2f}".format(profit))