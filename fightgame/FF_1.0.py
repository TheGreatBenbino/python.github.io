from random import randint
begin = 1
while begin == 1:
    begin = begin - 1
    player_health = 100
    energy = 100
    monster_count = (randint(1, 5))

    while monster_count >= 1:
        while player_health != 0 and energy != 0:
            monster = (randint(1,15))
            
            if monster == 1 or monster == 6 or monster == 10 or monster == 13 or monster == 15:
                monster_type = "Grunt"
                monster_health = 10

            elif monster == 2 or monster == 7 or monster == 11 or monster == 14:
                monster_type = "Foot_soldier"
                monster_health = 20

            elif monster == 3 or monster == 8 or monster == 12:
                monster_type = "Knight"
                monster_health = 30

            elif monster == 4 or monster == 9:
                monster_type = "Assassin"
                monster_health = 40

            elif monster == 5:
                monster_type = "Dragon"
                monster_health = 50
                
            print ("You have run into a " + monster_type + ".  Would you like to attack, or run?")
            monster_count = monster_count - 1
            F_F = raw_input()
                 
            if F_F == "Attack" or F_F == "attack" or F_F == "a" or F_F == "A":
                print ("You chose to fight...")
                damage_dealt = (randint(10,50))
                health_loss = (randint(1,30 or 100))
                energy_loss = (randint(1,5))
                player_health = int(player_health) - int(health_loss)
                energy = int(energy) - int(energy_loss)
                        
                if player_health >= 1 and damage_dealt >= monster_health and energy >= 1:
                    print ("You have slaughtered the " + str(monster_type))
                    print ("Your health is " + str(player_health))
                    print ("Your current energy is " + str(energy))            
                
                elif player_health >= 1 and energy >= 1 and damage_dealt < monster_health:
                    print ("Your atempt to slay the " + str(monster_type) + " was unsuccessful.  He got away.")
                    print ("Your health is " + str(player_health))
                    print ("Your current energy is " + str(energy))
                        
                elif player_health <= 0 or energy <= 0:
                    print ("You have died")
                    retry = raw_input("Would you like to play again? Y/N")
                            
                    if retry == "Y" or retry == "y":
                        start()
                            
                    else:
                        print ("Okay, Bye")

            elif F_F == "run" or F_F == "Run" or F_F == "R" or F_F == "r":
                print ("You chose to flee, and are currently running from the " + str(monster_type))
                escape = (randint(1,3))
                        
                if escape >= 2:
                    health_loss = (randint(1,3))
                    energy_loss = (randint(1,10))
                    player_health = int(player_health) - int(health_loss)
                    energy = int(energy) - int(energy_loss)
                            
                    if player_health >= 1 and energy >= 1:
                        print ("You escaped!")
                        print ("Your health is " + str(player_health))
                        print ("Your current energy is " + str(energy))
                            
                    else:
                        print ("You have died")
                        retry = raw_input("Would you like to play again? Y/N")
                                
                        if retry == "Y" or retry == "y": 
                            start()
                                
                        else:
                            print ("Okay, Bye")
                    
                elif escape < 2:
                    health_loss = (randint(1,15))
                    energy_loss = (randint(1,10))
                    player_health = int(player_health) - int(health_loss)
                    energy = int(energy) - int(energy_loss)
                            
                    if player_health >= 1 and energy >= 1:
                        print ("You tried to escape the " + str(monster_type) + ", but he caught up to you")
                        print ("You lost " + str(health_loss) + " health before you managed to kill the " + str(monster_type))
                        print ("Your health is " + str(player_health))
                        print ("Your current energy is " + str(energy))

                    elif player_health <= 0 or energy <= 0:
                        print ("In a Futile atempt to escape the wrath of the " + str(monster_type) + ", you died")
                        retry = raw_input("Would you like to play again? Y/N")
                            
                        if retry == "Y" or retry == "y":
                            start()
                            
                        else:
                            print ("Okay, Bye")
            else:
                decide = (randint(1,2))
                if decide == 1:
                    decision = "Run"
                elif decide == 2:
                    decision = "Fight"
                print ("You were forced to " + decision + ".  Remember to type 'f' or 'r'")    
    if monster_count >= 0:
        print("You have made it back home!")
        retry = raw_input("Would you like to play again? Y/N")
                            
        if retry == "Y" or retry == "y":
            start()
                            
        else:
            print ("Okay, Bye")

start()
