from random import randint 

while True:
  computerChoice = randint(1,10)
  userChoice = int(input("Enter Number: "))
  
  print("Computer Choice:", computerChoice)
  
  if computerChoice == userChoice:
    print ("you won")
  else:
    print("you lost")
