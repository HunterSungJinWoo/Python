
answer = input('Would you like to play ? (yes/no) ')

if answer.lower().strip() == 'yes':
    
    answer = input('You reach a crossroads, would you like to go left or right ?')
    if answer == 'left':
        answer = input('You encounter a monster, would you like to attack or run ?')
        
        if answer == 'attack':
            print('That was not the greatest idea, you lost! ')
        else:
            print('Good choice, you escaped safely.')
            
            
            
else:
    print("That's too bad")
        
        