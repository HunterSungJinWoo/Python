player = {'name' :  'vlad' , 'attack' : 13, 'heal' : 19 , 'health' : 100}
monster = {'name' :  'Troll' , 'attack_min' : 15, 'attack_max' :20,  'health' : 100}

answer = input('Would you like to play ? (yes/no) ')

if answer.lower().strip() == 'yes':
    print('---' * 8)
    import time
    time.sleep(2)                       
    print('Enter player name')
    time.sleep(2)
    print('---' * 8)
    time.sleep(2)
    player['name'] = input( )
    print('****' * 8)
    time.sleep(2)

    answer = input('You reach a crossroads, would you like to go left or right ?')
    if answer == 'left':
        time.sleep(2)
        answer = input('You encounter a Troll, would you like to attack or run ?')
        
        if answer == 'attack':
            time.sleep(2)
            print("That wasn't the greatest idea !")
            
        if answer == 'run':
            time.sleep(2)
            print('You escaped! ')  
    
    if answer == 'attack':
        time.sleep(2)
        from random import randint

        game_running = True
        game_results = []

        def calculate_monster_attack(attack_min, attack_max):
            return randint(monster['attack_min'], monster['attack_max'])

        def game_ends(winner_name):
            print(f'{winner_name} won the game')
            
        while game_running == True:
            counter = 0
            new_round = True
            player = {'name' :  'vlad' , 'attack' : 13, 'heal' : 16 , 'health' : 100}
            monster = {'name' :  'Troll' , 'attack_min' : 10, 'attack_max' :20,  'health' : 100}
              
             
            print('****' * 8)
            
            print('---' * 8)
            print(player['name'] + ' has ' + str(player['health']) + ' health')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health')
            print('---' * 8)
            
            print('****' * 8)
            
            while new_round == True:
                
                counter = counter + 1
                player_won = False
                monster_won =False

                print('---' * 8)
                print('Please select action')
                print('1) Attack' )
                print('2) Heal' )
                print('3) Exit')
                print('4) Show Results')

                player_choice = input( )
        #----------------------------------------------------------------------------------
                if player_choice == '1':
                    monster['health'] = monster['health'] - player['attack']
                    if monster['health'] <=0:
                        player_won = True
         #----------------------------------------------------------------------------------           
                    else:
                        player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], ['attack_max'])
                        if player['health'] <= 0:
                            monster_won = True
        #----------------------------------------------------------------------------------                  
                elif player_choice == '2':
                    player['health'] = player['health'] + player['heal']
                    monster_attack = randint(monster['attack_min'], monster['attack_max'])
                    
                    player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], ['attack_max'])
                    if player['health'] <0:
                        monster_won = True
        #----------------------------------------------------------------------------------            
                elif player_choice == '3':
                    new_round = False
                    game_running = False
        #----------------------------------------------------------------------------------            
                elif player_choice == '4':
                    for item in game_results:
                        print(item)
         #----------------------------------------------------------------------------------
         #----------------------------------------------------------------------------------
                elif player_choice == '0':
                    monster['health'] = monster['health'] - 100
                    if monster['health'] <=0:
                        player_won = True
        
                else :
                    print('Invalid Input')
                    
         #----------------------------------------------------------------------------------           
                if player_won == False and monster_won == False:
                    print(player['name'] + ' has ' + str(player ['health']) + 'left')
                    print(monster['name'] + ' has ' + str(monster ['health']) + 'left')
                    
                elif player_won:
                        game_ends(player['name'])
                        round_result = {'name' : player['name'], 'health' : player['health'], 'rounds' : counter}
                        game_results.append(round_result)
                        new_round = False 
        #----------------------------------------------------------------------------------                
                elif monster_won:
                        game_ends(monster['name'])
                        round_result = {'name' : player['name'], 'health' : player['health'], 'rounds' : counter}
                        game_results.append(round_result)
                        print(game_results)
                        new_round = False
                        
                if player_won == True or monster_won == True:
                        new_round = False
                if player_won == True :   
                        chest = input('You found a tereasure chest, would you like to check it (yes/no)? ')
                        
                        if chest == 'no':
                            print("You chosed to don't check it")
                            time.sleep(5)
                            print("Here is your punishment")
                            time.sleep(5)
                        
                        if chest == 'yes':
                            import time
                            time.sleep(2)
                            print('*')
                            time.sleep(2)
                            print('*')
                            time.sleep(2)
                            print('*')   
                            time.sleep(2)
                            print('*')
                            time.sleep(2)
                            print('*')         
                            print("It's locked")
                            print("You need a key")
                            print('****' * 8)
                            print('You hear a strange noice')
                            
                            noise = input('Would you like to hide (yes/no) ?')
                            if noise == 'yes':
                                print('You hided behind the bushes')
                                time.sleep(2)
                                print('Each time the sound gets louder')
                                time.sleep(2)
                                print('and')
                                time.sleep(2)
                                print('It was just a squirrel')
                                print(' The squirrel had a key in his mouth')
                                time.sleep(2)
                                print('He dropped it and run away')
                                print('You picked up the key')
                                time.sleep(2)
                                print('*')   
                                time.sleep(2)
                                print('*')
                                time.sleep(2)
                                print('*') 
                                print('You used the key')
                                time.sleep(2)
                                print('and the chest was oppened')
                                print('--You got an Iron sword--')
                            if noise == 'no':
                                print('It was just a squirrel')
                                print(' The squirrel had a key in his mouth')
                                time.sleep(2)
                                print('He dropped it and run away')
                                print('You picked up the key')
                                time.sleep(2)
                                print('*')   
                                time.sleep(2)
                                print('*')
                                time.sleep(2)
                                print('*') 
                                print('You used the key')
                                time.sleep(2)
                                print('and the chest was oppened')
                                print('--You got an Iron sword--')
                        
                
                        
    if answer == 'right':
        chest = input('You found a tereasure chest, would you like to check it (yes/no)? ')
        
        if chest == 'no':
            print("You chosed to don't check it") 
        
        if chest == 'yes':
            import time
            time.sleep(2)
            print('*')
            time.sleep(2)
            print('*')
            time.sleep(2)
            print('*')   
            time.sleep(2)
            print('*')
            time.sleep(2)
            print('*')         
            print("It's locked")
            print("You need a key")
            print('****' * 8)
            print('You hear a strange noice')
            
            noise = input('Would you like to hide (yes/no) ?')
            if noise == 'yes':
                print('You hided behind the bushes')
                time.sleep(2)
                print('Each time the sound gets louder')
                time.sleep(2)
                print('and')
                time.sleep(2)
                print('It was just a squirrel')
                print(' The squirrel had a key in his mouth')
                time.sleep(2)
                print('He dropped it and run away')
                print('You picked up the key')
                time.sleep(2)
                print('*')   
                time.sleep(2)
                print('*')
                time.sleep(2)
                print('*') 
                print('You used the key')
                time.sleep(2)
                print('and the chest was oppened')
                print('--You got an Iron sword--')
                print("Congratulations, you finished the demo")
                print('This was created by Vlad 4TPIFI')
                game_running = False
                new_round = False
                
            if noise == 'no':
                print('It was just a squirrel')
                print(' The squirrel had a key in his mouth')
                time.sleep(2)
                print('He dropped it and run away')
                print('You picked up the key')
                time.sleep(2)
                print('*')   
                time.sleep(2)
                print('*')
                time.sleep(2)
                print('*') 
                print('You used the key')
                time.sleep(2)
                print('and the chest was oppened')
                print('--You got an Iron sword--')
                time.sleep(25)
                
print("Congratulations, you finished the demo")
print('This was created by Vlad 4TPIFI')
game_running = False
new_round = False
                
        
                   

    
    
                


