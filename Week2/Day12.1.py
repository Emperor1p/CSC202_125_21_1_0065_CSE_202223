

enemies = 1
def increase_enemies():
    
    print(f"enemies inside function: {enemies}")
    return enemies + 2
enemies = increase_enemies()
print(f"enemies outside function: {enemies} ")

#local scope

potion_strength = 5
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion()
print(potion_strength)


#global variable

enemies = 1
def increase_enemies():
   
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies} ")


#another one

player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()
print(player_health)

###########################################

game_level = 3
def create_enemies():
    
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5: 
        new_enemy = enemies[0]
    print(new_enemy)



def set_difficulty():
    

