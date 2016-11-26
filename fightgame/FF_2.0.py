game_num = 0
if game_num < 1:
    play = raw_input("would you like to play a game?  y/n  ")
elif game_num > 0:
    play = raw_input("Would you like to play again?  y/n  ")
    
while play == "y":    
    
    import random
    class Adventurer(object):
        def __init__(self, name, health, damage, speed, level, xp_amount):
            self.name = name
            self.health = health
            self.damage = damage
            self.speed = speed
            self.level = level
            self.xp_amount = xp_amount
    player = Adventurer("bob", 100, 20, 20, 1, 1)

    
    
    class Monster(object):
        def __init__(self, name, health, damage, speed, xp, min_level):
            self.name = name
            self.health = health
            self.damage = damage
            self.speed = speed
            self.xp = xp
            self.min_level = min_level

    grunt = Monster("grunt", 100, 10, 5, 100, 1)
    foot_soldier = Monster("foot_soldier", 200, 20, 10, 20, 3)
    knight = Monster("Knight", 300, 30, 30, 30, 5)
    assassin = Monster("Assassin", 250, 30, 20, 25, 4)
    dragon = Monster("Dragon", 500, 100, 50, 200, 7)

    monsters = [grunt, foot_soldier, knight, assassin, dragon] 

    player_health = player.health
    player_damage = player.damage
    while player_health > 0:
        def get_monster(monsters):
            return (random.choice(monsters))

        monster_type = get_monster(monsters)
        while monster_type.min_level > player.level:
            monster_type = get_monster(monsters)


        monster_health = (monster_type).health
        monster_damage = (monster_type).damage
            
        print ("You have run into a " + (monster_type.name))
        print ("type 'h' to hit, 'r' to run")
        while monster_health > 0:
            decision = raw_input("")
            if decision == "h":
                player_health = int(player_health) - int(monster_damage)
                monster_health = int(monster_health) - int(player_damage)
                print ("Your health: " + str(player_health))
                print ("Monster health: " + str(monster_health))
            elif decision == "r":
                if player.speed > monster_type.speed:
                    print ("You have escaped the " + str(monster_type))
                elif player.speed < (monster_type).speed:
                    print ("You have failed to escape the " + str(monster_type))
                    player_health = int(player_health) - int(monster_damage)
                    monster_health = int(monster_health) - int(player_damage)
                    print "Your health: " + player.health
                    print "Monster health" + (monster_type).health
    
        if monster_health < 1:
            print ("You have killed the " + monster_type.name)
            player.xp_amount = int(player.xp_amount) + int(monster_type.xp)
            if int(player.xp_amount) == int(player.level) * 100:
                player.level = int(player.level) + 1
                print ("Your level is: " + player.level)

    if player.health < 1:
        print("You have died")
        exit

                
