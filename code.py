
answer = input('Wanna play/ (yes/no)')

if answer.lower().strip() == 'yes':
    answer = input('You reach a crossroads. What now, left or right?'). lower().strip()
    if answer == 'left':
        answer = input('You met a monster. Would you like to run or attack?')
        if answer == 'attack':
            print('That is the MONSTER, idiot! You lost!')
        else:
            print('Good choice. Your safety now. Wait for another game.')
    elif answer == 'right':
        print('You walk aimlessly to the right and fall on a patch of ice. You injure your leg and you not continue. '
              'The game OVER!')
    else:
        print('Invalid choice!')

else:
    print('END')

