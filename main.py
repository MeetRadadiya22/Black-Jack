import os
import random
from art import logo

print(logo)
start_game = True
while start_game == True:

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  userCards = []
  computerCards = []
  result = ""
  # ----------------------FUNCTIONS----------------------------

  #function which dealts the card to both computer and user
  def dealt_cards(userORcomputer):
    if userORcomputer == "user":
      for i in range(0,2):
        randomCard = random.choice(cards)
        userCards.append(randomCard)
        
      return userCards
    else:
      for j in range(0,2):
        randomCard = random.choice(cards)
        computerCards.append(randomCard)
        
      return computerCards[0]

  #function draw to draw cards
  def draw(userORcomputer):
    
    if userORcomputer == "user":
      randomCard = random.choice(cards)
      userCards.append(randomCard)
      return userCards

    else:
      randomCard = random.choice(cards)
      computerCards.append(randomCard)
      return computerCards
    
  # function total that totals the points
  def total(userORcomputer):

    total_User_Points = 0
    total_Computer_Points = 0
    if userORcomputer == "user":
      for points in userCards:
        total_User_Points += points
      return total_User_Points
    elif userORcomputer == "computer":
      for points in computerCards:
        total_Computer_Points += points
        
      return total_Computer_Points
  #----------------------------------------------------------
  start  = input("Type 'START' to enter the game: ")
  if start == "START":
    os.system('cls')
    #print statements to user cards and computer's one card.  
    print(f"\nYour cards are: {dealt_cards("user")}\n")
    print(f"Computer's card is: [{dealt_cards("computer")}]\n")

    draw_user = True
    while draw_user == True:
      #input for user if he wants to draw card.
      draw_card = input("Do you want to draw card? 'Y' or 'N': ")
      
      if draw_card == "Y":
        print(f"\nYour cards are: {draw("user")}")
        #checking if the user's total exceeds 21 then it looses.
        if total("user") > 21:
          draw_user = False
          result = "you loose."

        elif total("user") == 21:
          draw_user = False
          result = "you win."

      #if the user says not to draw then compare the both the totals.
      elif draw_card == "N":
        
        draw_user = False
        # if the computer's total is < 17 then computer draws the card 
        #and if it greater than 17 then it compares who has highest points.
        draw_computer = True
        while draw_computer == True:
          if total("computer") < 17:
            draw("computer")
          else:
            draw_computer = False
            if total("user") == total("computer"):
              result = "PUSH"
            elif total("computer") > 21:
              result = "you win."
            elif total("user") > total("computer"):
              result = "you win."
            elif total("computer") > total("user"):
              result = "you loose."
      else: 
        print("INVALID INPUT!")

    #print the result
    print(f"\ncomputer's cards are{computerCards}")
    print(f"\nyour total is {total("user")}")
    print(f"\ncomputer's total is {total("computer")}\n")
    print(result)

    play_again = input("\nDo you want to play again? 'Y' or 'N': ")
    if play_again == "Y":
      start_game = True
      os.system('cls')
    elif play_again == "N":
      start_game = False
    else:
      print("INVALID INPUT!")
  
  else:
    print("INVALID INPUT!")
    

    
    
  
  
   




