def RockPaperScissors(ans):
    import random
    x=random.choice(["Rock","Paper","Scissors"])

    while ans!=x:
         if x == "Rock":
                if ans == "Scissors":
                    return("You Lose"),x
                else:
                    return("You win"),x                  
         elif x == "Paper":
                if ans == "Rock":
                    return("You lose"),x               
                else:
                     return("You win"),x               
         elif x == "Scissors":
                if ans == "Rock":
                     return("You win"),x               
                else:
                     return("You lose") ,x 
                                           
                                                         
                                                    
    if x==ans:
      return("Fair"),x

   







