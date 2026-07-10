import random

#key value
 #r= 👊
 #p= ✋
 #s= ✌️
emojies= {'r': '👊', 'p': '✋', 's': '✌️'}
choices=['r', 'p', 's']

while True:
    user_choice = input('Rock, Paper, or Scissors?(r/p/s): ').lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose 'r', 'p', or 's'.")
        continue

    computer_choice = random.choice(choices)

    print(f'You choose {emojies[user_choice]}')
    print(f'Computer choose {emojies[computer_choice]}')
    if user_choice == computer_choice:
        print("It's a tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's')or 
        (user_choice == 'p' and computer_choice == 'r')or
        (user_choice == 's' and computer_choice == 'p')):
        print("You Win!")
    else:
        print("You Lose!")   

    should_continue = input('Continue?(n/y): ').lower() 
    if should_continue == 'n':
       break
      