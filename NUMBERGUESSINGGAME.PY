import random
cnumber=random.randrange(1,101)

userInput=int(input("Enter Your Number:--- "))
if userInput>cnumber:
    print("Computer Number",cnumber)
    print("Your guess number is high")
elif cnumber>userInput:
  print("Your guess number is too low")
else:
  print("Your guess number is equal") 