VM = { 1: ["Coke", 2.50], 2: ["Cherry", 2.00] , 3 : ["Sprite", 2.25] , 4: ["Water", 3.00]}
price=2.00

def payment(name, cost):
  pay = 0.0
  while pay < cost:
    pay += float(input("Insert money: "))
    if pay < cost:
      total = cost - pay
      print("Need more money ", str(total))
  print("Payment completed")
  if pay > cost:
    total = pay - cost
    print("Your change is: ", str(total))
  print("Enjoy your ", name)

def menu():
  print("Welcome to this Vending Machine")
  print("Make a selection")
  print(" 1. Coke \n 2. Cherry \n 3. Sprite \n 4. Water")


def user_selection(user_input):
  name = ""
  price = ""
  if user_input == 1:
      name, price = VM[user_input]
      print("You picked a " , name)
      print("Your cost is ", str(price))
       
  elif user_input == 2:
     name, price = VM[user_input]
     print("You picked a ", name)
     print("Your cost is ", str(price))
  elif user_input == 3:
    name, price = VM[user_input]
    print("You  picked a ", name)
    print("Your cost is ", str(price))
  elif user_input == 4:
    name, price = VM[user_input]
    print("You picked a ", name)
    print("Your cost is ", str(price))
  else:
    print("Wrong entry.")
    return True
  
  payment(name, price)
  return False
      
menu()
invalid_seleccion = True
while invalid_seleccion:
  user = int(input("Make your selection: "))
  invalid_seleccion = user_selection(user)
