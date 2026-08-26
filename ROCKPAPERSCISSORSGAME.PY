import random 
l=["rock","scissor","paper"] 
 
 
while True : 
  ccount=0 
  ucount=0 
  uc=int(input('''  
              GAME START...... 
              1 YES 
              2 NO |EXIT ''')) 
  if uc==1: 
    for a in range(1,6): 
      userInput=int(input('''  
                           
                1 ROCK 
                2 SCISSOR 
                3 PAPER  
                               ''')) 
      if userInput==1: 
        uchoice="rock" 
      elif userInput==2: 
        uchoice="scissor" 
      elif userInput==3: 
        uchoice="paper" 
     
     
      Cchoice=random.choice(l) 
      if  Cchoice==uchoice: 
        print("Computer value",Cchoice) 
        print("User Value",uchoice) 
        print("Game Draw") 
        ucount=ucount+1 
        ccount=ccount+1 
      elif (uchoice=="rock" and Cchoice=="scissor")or(uchoice=="paper" and Cchoice=="rock")or(uchoice=="scissor" and Cchoice=="paper"): 
     
        print("Computer value",Cchoice) 
        print("User Value",uchoice) 
        print("You Win") 
        ucount=ucount+1 
         
         
      else: 
        print("Computer value",Cchoice) 
        print("User Value",uchoice) 
        print("Computer Win") 
        ccount=ccount+1 
     
  if (ucount==ccount) :  
      print("Final Game Draw ....")
      print("User count",ucount)
      print("Computer count",ccount)
  elif(ucount>ccount):
            print("Final Game YOU WIN ....")
            print("User count",ucount)
            print("Computer count",ccount)
  elif (ucount>ccount):
             print("Final Game YOU WIN ....")
             print("User count",ucount)
             print("Computer count",ccount)
      
  else: 
    break