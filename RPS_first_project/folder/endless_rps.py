import random

def rockpaperscissors():
    computer_count = 0
    user_count = 0
    user_name = input('Please enter your name: ')

    while True:
        player_choice = ['scissors', 'paper', 'rock']
        ai_choice = random.choice(player_choice)
        user_choice = input('(1) Scissors \n(2) Paper \n(3) Rock\nType your choice: ').lower()

        if user_choice == '2' or user_choice.lower() == 'paper':
            user_choice = 'paper'
        elif user_choice == '3' or user_choice.lower() == 'rock':
            user_choice = 'rock'
        elif user_choice == '1'or user_choice.lower() == 'scissors':
            user_choice = 'scissors'
        else:
            print('Invalid selection, please try again\n')
            continue

        print(f'You played {user_choice}, the computer played {ai_choice}\n')
        if user_choice == 'scissors' and ai_choice == 'rock' or \
            user_choice == 'paper' and ai_choice == 'scissors' or \
            user_choice == 'rock' and ai_choice == 'paper':
            print('Computer Win')
            computer_count += 1

        elif user_choice == 'rock' and ai_choice == 'scissors' or \
            user_choice == 'scissors' and ai_choice == 'paper' or \
            user_choice == 'paper' and ai_choice == 'rock':
                print('You Win')
                user_count += 1

        elif user_choice == ai_choice:
                print('Tie')
        
        print(f'Robot: {computer_count} -', user_name,f': {user_count}')
        print()

# rockpaperscissors()