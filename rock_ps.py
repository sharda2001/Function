from random import randint
def win():
     print ('You win!')
def lose():
    print ('You lose!')
while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    if player_choice == computer_choice:
        print("computer choice is:",computer_choice)
        print ('Draw!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("computer choice is:",computer_choice)
        win()
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print("computer choice is:",computer_choice)
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("computer choice is:",computer_choice)
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print("computer choice is:",computer_choice)
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("computer choice is:",computer_choice)
        win()
    elif player_choice == "paper"  and computer_choice == "scissor":
        print("computer choice is:",computer_choice)
        lose()
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break
win() 

 

