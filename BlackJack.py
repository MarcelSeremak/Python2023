import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
start = input("Do you want to play BlackJack with me? type 'y' if yes, type 'n' in not:  ")
while True:
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
    ### QUESTION IF THE PLAYER WANTS TO PLAY A GAME
    if start=="n":
        print("Okey, I get it. Bye")
        break
        ### THE GAME ENDS HERE
    if start=="y":
        your_cards=[random.choice(cards),random.choice(cards)]
        computer_cards=[random.choice(cards), "X"]
        print(f"Your cards : {your_cards}")
        print(f"Computer cards: {computer_cards}")
        question=input("If you want to grab another card write 'y', if not, write 'n':  ")
        if question=="y":
            your_cards.append(random.choice(cards))
        print(your_cards)
        computer_cards[1]=random.choice(cards)
        print(computer_cards)
        player_points=0
        computer_points=0
        for i in your_cards:
            player_points=player_points+i
        for j in computer_cards:
            computer_points=computer_points+j
        if player_points>21 and computer_points>21:
            print("It's a draw")
        elif player_points<=21 and player_points>computer_points:
            print("You win! Congratulations!!!")
        elif player_points<=21 and player_points<computer_points and computer_points<=21:
            print("You lost...")
        elif player_points>21 and computer_points<21:
            print("You lost...")
        elif player_points==computer_points and player_points<=21:
            print("It's a draw")
        decision=input("Do you want to play again? Type 'y' if yes, type 'n' if not:  ")
        if decision=="n":
            print("Okey, see you next time!")
            break
        if decision=="y":
            print("Hurraay, so let's play again\n")
