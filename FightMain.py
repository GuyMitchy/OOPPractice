# Class Practice - Fighters

# Here i am going to outlined how classes work and practice using them by making objects, in this case, types of fighters, fight each other.

# Classes are used to construct objects. 
# They are like blueprits for how objects behave.
# Each class is a type of object.
# A class decides what parameter and attributes an object has.
# It then decides how the object will behave, using methods.
import time
import random
import sys
# First we define a class like this
class Fighters():
# Then we initialise the class with all the parameters that each object of this class has.
# The self parameter allows the class to refernce itself, meaning all passed in parameters become global wthin the class.  
    def __init__(self, name, hp, ap, strength, defense, level):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.strength = strength
        self.defense = defense
        self.original_hp = hp
        self.original_ap = ap
        self.level = level
        self.is_charging = False
        self.is_defending = False
        self.hp_scaler = 0
        self.strength_scaler = 0
        self.defense_scaler = 0
        self.is_melting = False     
        self.is_shocked = False 
        self.is_bleeding = False
            
    def take_damage(self, damage):
        damage -= self.defense
        if damage < 0:
            damage = 0
        damage = round(damage)
        self.hp -= damage
        self.hp = round(self.hp)
        if self.hp < 0:
            self.hp = 0
        time.sleep(0.8)
        print(f"{self.name} takes {damage} damage")
        time.sleep(0.8)
        print(f"{self.name} has {self.hp} HP")
        if player_character.hp == 0:
            print(" ")
            time.sleep(0.8)
            print(f"{self.name} has died....")
            print (" ")
            time.sleep(2)
            print("-------GAME OVER-------")
            sys.exit()
       
        if self.hp <= 0:
            raise FightOverException
        

    def attack(self, target):
        if self.is_charging:
              print ((f"{self.name} executes a turbocharged attack on {target}"))
        else:
                print(f"{self.name} attacks {target}")
        print(" ")
        time.sleep(0.8)
        damage = self.strength * 3  # will ad more complex damage computation later
        target.take_damage(round(damage))

    def defend(self):
        self.defense *= 1.5  # increase defense by half.
        self.is_defending = True  # Set a flag indicating that the human is currently defending.
        print(f"{self.name} is holding steadfast and defending for this turn.")
        time.sleep(0.8)
        print(" ")
        print(f"Defense has increased to {round(self.defense)}!") # round defens evalue just for printing.
        time.sleep(0.8)
        print(" ")

    def stop_defending(self):
        if self.is_defending:  # If the Fighter is currently defending...
            self.defense /= 1.5  # ...divide by 1.5 to bring it back to its original value.
            self.defense = int(self.defense) # when dividing by a float you get a float. 
                                            #i know this value will always be an int represented as a float. so int removes the .0
            print(f"Defense has returned to {self.defense}")
            self.is_defending = False  # Clear the defending flag.

    def enemy_is_crippled(self):

        crippled_strength_modifier = self.strength * 0.2  
        crippled_defense_modifier = self.defense * 0.2 
        crippled_strength_modifier = round(crippled_strength_modifier)  
        crippled_defense_modifier = round(crippled_defense_modifier)
        self.strength -= crippled_strength_modifier
        self.defense -= crippled_defense_modifier   
        print(f'{self.name} is crippled!')
        time.sleep(0.8)
        print(f'Strength: -{crippled_defense_modifier}')
        time.sleep(0.8)
        print(f'Defense: -{crippled_defense_modifier}')
        time.sleep(0.8)

    def enemy_is_hurt(self):  # used for shocked as well as melting
            # this only runs at the start of the enmy turn after checking if they are melting with. if enemy.is_melting == True
            hurt_hp_modifier = 5 # set how much hp enemy loses when melting
            self.hp -= hurt_hp_modifier # remove the melting modifier from hp
            if self.hp < 0:
                self.hp = 0
            if self.is_shocked == True:
                print(f'{self.name} is shocked!. -{hurt_hp_modifier}HP') 
            elif self.is_melting == True:
                print(f'{self.name} is melting! -{hurt_hp_modifier}HP')
            elif self.is_bleeding == True:
                print(f'{self.name} is bleeding! -{hurt_hp_modifier}HP')
            time.sleep(0.8)
            print(" ")
            print(f"{self.name} has {self.hp}HP")
            
            
    
    def charge(self):
        self.strength *= 1.4
        self.ap += 1
        player_character.is_charging = True
        print(f"{self.name} is charging up for big damage on the next turn.")  
        time.sleep(0.8)
        print(" ")
        print(f"Strength has increased to {round(self.strength)}")
        print(" ")

    def stop_charging(self):
        if self.is_charging:
            self.strength /= 1.4  # ...bring strength back to its original value.
            print(" ")
            time.sleep(0.8)
            print(f"{self.name} stopped charging")
            print(" ")
            time.sleep(0.8)
            print(f"Strength has returned to {round(self.strength)}")
            print(" ")
            self.is_charging = False  # Clear the defending flag.


    def spec_attack(self, target):
        pass

    def charged_spec_attack(self, target):
        pass
    
    def reset_player_character(self): 
        self.stop_charging()
        self.stop_defending()
        
        if self.level == 1: 
            self.hp = self.original_hp
            self.ap = self.original_ap
        else:
            self.hp = self.original_hp * (1.15 ** (self.level - 1))
            self.ap = self.original_ap + self.level - 1
            self.hp = round(self.hp)

        print(" ")
        time.sleep(0.8)
        print (f"HP and AP reset")
        time.sleep(0.8)
        print(" ")

    def level_up(self): 
        self.level += 1       
        self.hp_scaler = self.hp * 1.35
        self.hp = round(self.hp_scaler)
        self.ap += 1
        self.strength_scaler = self.strength * 1.35  # needs looking at.
        self.strength = round(self.strength_scaler)
        self.defense_scaler = self.defense * 1.35
        self.defense = round(self.defense_scaler)
        self.heal_amount += 10 
        time.sleep(2)
        print(" ")
        print(" ")
        print(f"-------LEVEL UP-------")
        print(" ")
        print(" ")
        time.sleep(0.8)
        print(f"{self.name} is now level {self.level}")
        print(" ")
        time.sleep(0.8)
        print(f"HP: {self.hp}")
        time.sleep(0.5)
        print(f"AP:{self.ap}")
        time.sleep(0.5)
        print(f"Strength: {self.strength}")
        time.sleep(0.5)
        print(f"Defense: {self.defense}")
        time.sleep(0.5)
        print(" ")
        print(f"Bandages now heal {self.heal_amount}HP")
   
    def find_bandages(self):    # Used to be in human class and robo class but just added to fighters class with an isinstace check to determine which class for different message.
                if isinstance(player_character, Robo):
                    self.num_bandages += 2 
                    time.sleep(2)
                    print(" ") 
                    print(f"'Hey {self.name}!'")
                    time.sleep(2)
                if isinstance(player_character, Robo): 
                    print(" ")
                    print(f"2 reapir kits were tossed at {self.name} by someone in the crowd.")
                    time.sleep(2)
                    print(" ")
                    print(f"repair kits increase to {self.num_bandages}")
                else:
                    print(" ")
                    print(f"2 bandages were tossed at {self.name} by someone in the crowd.")
                    time.sleep(2)
                    print(" ")
                    print(f"Bandages increase to {self.num_bandages}")
  
class Human(Fighters):
   
    
    def __init__(self, name, hp, ap, strength, defense, level, num_bandages):
        super().__init__(name, hp, ap, strength, defense, level)
        self.num_bandages = num_bandages
        self.is_defending = False
        self.turn_counter = 0
        self.xp = 0
        self.heal_amount = 15

    def __str__(self):
        return self.name

    def get_stats(self, hp, ap, strength, defense, num_bandages):
        return (f"HP: {hp}"), (f"Attribute Points: {ap}"), (f"Strength: {strength}"), (f"Defense: {defense}"), (f"Bandages: {num_bandages}")
   
    def get_num_bandages(self):
        if self.num_bandages > 0:
            return True
        else:
             return False 
   
    def heal(self):  # doesnt account for healing to above original hp
        if self.get_num_bandages() == True:
            self.hp += self.heal_amount # heal by heal amount which is increased for each level

            if self.hp > self.original_hp * (1.15 ** (self.level - 1)): 
                self.hp = self.original_hp * (1.15 ** (self.level - 1))  # this accounts for healing above max hp for each level.
                self.hp = round(self.hp)
            self.num_bandages -= 1
            time.sleep(0.8)
            print(" ")
            print (f"{self.name} has used a bandage to heal for {self.heal_amount}HP. HP restored to {self.hp}HP")
            print(" ")

        else:
            time.sleep(0.8)
            print(" ")
            print(f"{self.name} tried to heal but has no bandages")
            time.sleep(0.8)

   
class Archer(Human):
    def __init__(self, name, hp, ap, strength, defense, level, num_bandages, num_arrows):
            super().__init__(name, hp, ap, strength, defense, level, num_bandages)
            self.num_arrows = num_arrows
    
    def spec_attack(self, target): 
        if self.num_arrows > 0:
            if self.ap > 0:
              print (f"{self.name} fires a piercing shot straight through {target.name}'s defenses.")  
              print(" ")
              damage = self.strength * random.uniform(4.5,5)  # base attack is self.strength * 3
              self.ap -= 1
              self.num_arrows -= 1
              target.take_damage(round(damage))
              time.sleep(0.8)
              print(f"{self.name} has {self.ap} AP")
              time.sleep(0.8)
              print(" ")
              print (f"{self.name} has {self.num_arrows} arrows left.")
              time.sleep(0.8)
              print("")
              return True
            
            else: 
                print(f"{self.name} tried to execute a special attack but doesn't have enough AP")
                return False
                #start cycle again

        else:
            time.sleep(0.8)
            print("")
            print(f"{self.name} tried to execute a special attack but doesn't have enough arrows") 
            time.sleep(0.8)
            print("") 
            
            
    def charged_spec_attack(self, target):
        if self.num_arrows > 0: 
            if self.ap >= 2:
                print (f"{self.name} shoots a supercharged lightning arrow at {target.name}'s chest.")
                damage = self.strength * random.uniform(4, 4.5)
                self.ap -= 2
                self.num_arrows -= 1
                target.take_damage(round(damage))
                print(' ')
                target.enemy_is_crippled()
                print(" ")
                time.sleep(0.8)
                print(f"{target.name} is shocked!")
                print(" ")
                target.is_hurt = True
                target.is_shocked = True
                time.sleep(0.8)
                print(f"{self.name} has {self.ap} AP")
                time.sleep(0.8)
                print(" ")
                print (f"{self.name} has {self.num_arrows} arrows left.")
                time.sleep(0.8)
                print("")
                return True
            else: 
                print(f"{self.name} tried to execute a charged special attack but doesn't have enough AP")
                #start cycle again
                return False
        else:
            time.sleep(0.8)
            print("")
            print(f"{self.name} tried to execute a charged special attack but doesn't have enough arrows") 
            time.sleep(0.8)
            print("")
            return False    
                        
class Boxer(Human):
    def __init__(self, name, hp, ap, strength, defense, level, num_bandages):
             super().__init__(name, hp, ap, strength, defense, level, num_bandages)
        
    def spec_attack(self, target):
        if self.ap > 0:
            print (f"Steel Uppercut!.")
            damage = self.strength * random.uniform(4, 4.5)
            self.ap -= 1
            target.take_damage(round(damage))
            if self.level > 2:
                print (f"{target.name} gets sent flying into the air, and comes crashing back down to the arena floor.")
                damage = self.strength
                target.take_damage()
            time.sleep(0.8)
            print(" ")
            print(f"{self.name} has {self.ap} AP")
            print(" ")
            time.sleep(0.8)
            return True
        else:
            print(f"{self.name} tried to execute a special attack but doesn't have enough AP")
            return False
        
    def charged_spec_attack(self, target):
        if self.ap >= 2:
            print (f"Blazing Fists!")
            self.ap -= 2
            damage = self.strength * random.uniform(2.5, 3)
            target.take_damage(round(damage))
            damage = self.strength * random.uniform(2.5, 3)
            target.take_damage(round(damage))
            damage = self.strength * random.uniform(2.5, 3)
            target.take_damage(round(damage))
            print(' ')
            target.enemy_is_crippled()
            time.sleep(0.8)
            print(f"{self.name} has {self.ap} AP")
            time.sleep(0.8)
            print(" ")
            return True
        else: 
            print(f"{self.name} tried to execute a charged special attack but doesn't have enough AP")
            #start cycle again
            return False
            
class Gunner(Human):
    def __init__(self, name, hp, ap, strength, defense, level, num_bandages, num_bullets, num_grenades):
            super().__init__(name, hp, ap, strength, defense, level, num_bandages)
            self.num_bullets = num_bullets
            self.num_grenades = num_grenades

    def spec_attack(self, target):
        if self.num_bullets > 2:
            if self.ap > 0:
                print (f"{self.name} uses 1 ap and fires an M16 at {target.name}.")
                self.ap -= 1
                print(" ")
                damage = self.strength * random.uniform(2.5, 3)
                target.take_damage(round(damage))
                damage = self.strength * random.uniform(2.5, 3)
                target.take_damage(round(damage))
                damage = self.strength * random.uniform(2.5, 3)
                target.take_damage(round(damage))
                self.num_bullets -= 3
                time.sleep(0.8)
                print("")            
                print(f"{self.name} has {self.ap} AP")  
                time.sleep(0.8)
                print("")
                print (f"{self.name} has {self.num_bullets} bullets left.")   
                time.sleep(0.8)
                print("")
                return True
            else:
                print(f"{self.name} tried to execute a special attack but doesn't have enough AP")
                return False
        else:
                time.sleep(0.8)
                print("")
                print(f"{self.name} tried to execute a special attack but doesn't have enough bullets") 
                time.sleep(0.8)
                print("")
                return False 
        
    def charged_spec_attack(self, target):  # i can do if level == 1 and level ==2 for differeent actions!!!
        if self.num_grenades > 0: 
            if self.ap >= 2:
                print(f"{self.name} takes cover and throws a frag grenade at {target.name}.")
                print(' ')
                if self.level > 3:                
                    time.sleep(0.8)
                    print("...")
                    time.sleep(0.8)
                    print("...")
                    time.sleep(0.8)
                    print("...")
                    print(f'{target.name} is almost blown to bits, but comes up laughing with a face full of steel.')  
                else:
                    print(f"It rolls straight between {target.name}'s feet.")
                    time.sleep(0.8)
                    print("...")
                    time.sleep(0.8)
                    print("...")
                    time.sleep(0.8)
                    print("...")
                    time.sleep(0.8)
                    print(' ')            
                          
                damage = self.strength * random.uniform(5, 5.5)
                self.ap -= 2
                self.num_grenades -= 1
                target.take_damage(round(damage))
                print(' ')
                target.enemy_is_crippled()
                time.sleep(0.8)
                print(' ')
                print(f"{self.name} has {self.ap} AP")
                time.sleep(0.8)
                print(" ")
                print (f"{self.name} has {self.num_grenades} grenades left.")
                time.sleep(0.8)
                print("")
                return True
            else: 
                print(f"{self.name} tried to execute a charged special attack but doesn't have enough AP")
                #start cycle again
                return False
        else:
            time.sleep(0.8)
            print("")
            print(f"{self.name} tried to execute a charged special attack but doesn't have any grenades") 
            time.sleep(0.8)
            print("")
            return False  
    
class Warrior(Human):
    def __init__(self, name, hp, ap, strength, defense, level, num_bandages):
            super().__init__(name, hp, ap, strength, defense, level, num_bandages)
             
    def spec_attack(self, target):
        if self.ap > 0:
            self.ap -= 1
            damage = self.strength * random.uniform(4, 5)

            print("Warrior's Rend!")
            time.sleep(0.8)
            print("")

            if self.level < 2:
                target.take_damage(round(damage))
            else:
                print("Warrior's Rend strikes twice!")
                time.sleep(0.8)
                print("")
                target.take_damage(round(damage))
                target.take_damage(round(damage))

            time.sleep(0.8)
            print("")
            print(f"{self.name} has {self.ap} AP")
            print(" ")
            return True
        else:
            print(f"{self.name} tried to execute a special attack but doesnt have enough AP")
            return False
        
    def charged_spec_attack(self, target):
        if self.ap >= 2 :
            print ("Thunderstrike Cyclone!")
            damage = self.strength * random.uniform(2.5, 3)
            self.ap -= 2
            damage = self.strength * random.uniform(2.5, 3)
            target.take_damage(round(damage))
            damage = self.strength * random.uniform(2.5, 3)
            target.take_damage(round(damage))
            damage = self.strength * random.uniform(2.5, 3)
            target.take_damage(round(damage))
            target.enemy_is_crippled()
            time.sleep(0.8)
            print(" ")
            print(f"{self.name} has {self.ap} AP")
            time.sleep(0.8)
            print(" ")
            print("")
            return True
        else: 
            print(f"{self.name} tried to execute a charged special attack but doesnt have enough AP")
            #start cycle again
            return False

# enemies only below, could make enemy class and use these as sublcasses. 
# if i make e.g. archer enemy sublass then enemies can have different moves !!
   
class Monster(Fighters):
      def __init__(self, name, hp, ap, strength, defense, level):
            super().__init__(name, hp, ap, strength, defense, level)

class Robo(Fighters):
        def __init__(self, name, hp, ap, strength, defense, level, num_bandages, laser_power, num_missiles):
            super().__init__(name, hp, ap, strength, defense, level)
            self.laser_power = laser_power
            self.num_missiles = num_missiles
            self.num_bandages = num_bandages
            self.is_defending = False
            self.xp = 0
            self.heal_amount = 10
            
        
        def __str__(self):
            return self.name
        
        def get_stats(self, hp, ap, strength, defense, num_bandages):
            return (f"HP: {hp}"), (f"Attribute Points: {ap}"), (f"Strength: {strength}"), (f"Defense: {defense}"), (f"Bandages: {num_bandages}")    
        
        def get_num_bandages(self):
            if self.num_bandages > 0:
                return True
            else:
                return False 
        
        def heal(self):  # doesnt account for healing to above original hp
            if self.get_num_bandages() == True:
                self.hp += self.heal_amount # heal by heal amount which is increased for each level
                if self.hp > self.original_hp * (1.15 ** (self.level - 1)): 
                    self.hp = self.original_hp * (1.15 ** (self.level - 1))
                    self.hp = round(self.hp)
                self.num_bandages -= 1
                time.sleep(0.8)
                print(" ")
                print (f"{self.name} has used a repair kit to heal for {self.heal_amount}HP. HP restored to {self.hp}HP")
                print(" ")

            else:
                time.sleep(0.8)
                print(" ")
                print(f"{self.name} tried to heal but has no repair kits")
                time.sleep(0.8)
       
        
            self.num_bandages += 2 
            time.sleep(2)
            print(" ") 
            print(f"'Hey {self.name}!'")
            time.sleep(2)
            print(" ")
            print(f"2 repair kits were paradopped in to {self.name} from the support chopper")
            time.sleep(2)
            print(" ")
            print(f"repair kits increase to {self.num_bandages}")
        
        def spec_attack(self, target):
            if self.laser_power > 0:
                if self.ap > 0:
                    print (f"{self.name} fires a high power laser straight through {target.name}.")
                    self.ap -= 1
                    print(" ")
                    damage = self.strength * random.uniform(4, 4.5)
                    target.take_damage(round(damage))
                    self.laser_power -= 10
                    time.sleep(0.8)
                    print("")            
                    print(f"{self.name} has {self.ap} AP")  
                    time.sleep(0.8)
                    print("")
                    print (f"{self.name} laser power is at {self.laser_power}%")   
                    time.sleep(0.8)
                    print("")
                    return True
                else:
                    print(f"{self.name} tried to execute a special attack but doesn't have enough AP")
                    return False  
            else:
                time.sleep(0.8)
                print("")
                print(f"{self.name} tried to execute a special attack, but their laser was out of power") 
                time.sleep(0.8)
                print("")
                return False 
            
        def charged_spec_attack(self, target):  # i can do if level == 1 and level ==2 for differeent actions!!!
            if self.num_missiles > 0: 
                if self.ap >= 2:
                    print(f"{self.name} fires a heat seeking nuke into the arena {target.name}.")
                    print(' ')
                    if self.level > 3:                
                        time.sleep(0.8)
                        print("--Target Locked--")
                        time.sleep(0.8)
                        print ("")
                        time.sleep(0.8)
                        print(" ")
                        print("BOOM!")
                        print(" ")
                        print(f"{target.name} is blasted with radiation")
                          # resets strength and defense so crippling works properly
                        
                        
                    else:  # change this later for new attack
                        time.sleep(0.8)
                        print("--Target Locked--")
                        time.sleep(0.8)
                        print ("")
                        time.sleep(0.8)
                        print(" ")
                        print("BOOM!")
                        print(" ")
                        print(f"{target.name} is blasted with radiation")
                        
                        
                        
                        
                    damage = self.strength * random.uniform(2.8, 3)
                    self.ap -= 2
                    self.num_missiles -= 1
                    target.take_damage(round(damage))
                    print(' ')
                    target.is_hurt == True
                    target.is_melting = True
                    print(f"{target.name} is melting")
                    time.sleep(0.8)
                    print(' ')
                    print(f"{self.name} has {self.ap} AP")
                    time.sleep(0.8)
                    print(" ")
                    print (f"{self.name} has {self.num_missiles} nukes left.")
                    time.sleep(0.8)
                    print("")
                    return True
                else: 
                    print(f"{self.name} tried to execute a charged special attack but doesn't have enough AP")
                    #start cycle again
                    return False
            else:
                time.sleep(0.8)
                print("")
                print(f"{self.name} tried to execute a charged special attack but doesn't have enough bullets") 
                time.sleep(0.8)
                print("")
                return False  


class Boss(Fighters):
      def __init__(self, name, hp, ap, strength, defense, level):
            super().__init__(name, hp, ap, strength, defense, level)


# Fight Logic Classes
            
class FightOverException(Exception):
    pass

class Fight:    # Contains player_start() (START and END), enemy_start() (START and END), player_turn(), enemy_turn()
    def __init__(self, player_character, enemy):
        self.player_character = player_character
        self.enemy = enemy
        self.turn_counter = 0

    def player_start(self):
        try:
            while self.player_character.hp > 0 and self.enemy.hp > 0:
                if self.player_character.is_charging == False:
                    self.player_turn()
                    self.enemy_turn()
                else:
                    self.charged_player_turn()
                    self.enemy_turn()
        except FightOverException:
            if self.enemy.hp <= 0:
                time.sleep(0.8)
                print(" ")
                print(f'{self.player_character} wins!')
            elif self.player_character.hp <= 0:
                time.sleep(0.8)
                print(f'{self.enemy} wins!')

    def enemy_start(self):
        try:
            while self.player_character.hp > 0 and self.enemy.hp > 0:
                if self.player_character.is_charging == False:
                    self.enemy_turn()
                    self.player_turn()                
                else:
                    self.enemy_turn()
                    self.charged_player_turn()
                    
                
        except FightOverException:
            if self.enemy.hp <= 0:
                time.sleep(0.8)
                print(f'{self.player_character.name} wins!')
            elif self.player_character.hp <= 0:
                time.sleep(0.8)
                print(f'{self.enemy} wins!')
        

    def fight_intro(self):
        pass  # No default intro

    def charged_player_turn(self):
        action = ""  # initialize action here
        while not action:
            time.sleep(0.8)
            print(' ')
            print(f"-----Player Turn-----")
            time.sleep(0.8)
            print(" ")
            print(f"{self.enemy.name} has {self.enemy.hp}HP")
            if player_character.is_charging: # check for charged or no. if charged run attack or charged spec attack.
                print(f"{self.player_character} is charged up... +1 AP!")
                print("Do you want to Attack or Special Attack (-2AP)")
                action = input().lower()
                self.turn_counter += 1
                print(" ")
                time.sleep(0.8) 
                
                if action == "attack":
                    print(" ")
                    player_character.attack(self.enemy)
                    time.sleep(0.8)
                    print(" ")
                    player_character.stop_charging()
                    print(" ")

                elif action == "special attack":
                    print(" ")
                    charged_spec_attack_success = self.player_character.charged_spec_attack(self.enemy)
                    if charged_spec_attack_success: # if enough ap, it runs the method and sets attack succes to true of false.
                        player_character.stop_charging() 
                        time.sleep(0.8)                        
                          
                    else:
                        action = ""
                else:
                    print(" ")
                    print('Invalid action!')
                    self.turn_counter -= 1
                    print(" ")
                    action = "" # reset action to loop input
                    time.sleep(0.8)  

                        # !!!!!!!!!!!!!!!!need to stop this from entering normal player turn cycle and go to enemy turn after charged attacks
    
    def player_turn(self):
        action = ""  # initialize action here
        while not action:
            time.sleep(0.8)
            print(' ')
            print(f"-----Player Turn-----")
            time.sleep(0.8)
            print(" ")
            print(f"{self.enemy.name} has {self.enemy.hp}HP")
            print(" ")
            time.sleep(0.8)
            print(" ")
            print("Do you want to Attack, Special Attack (-1AP), Charge, Defend, or Heal")
            print(" ")
            action = input().lower()
            self.turn_counter += 1 
            time.sleep(0.8)
        # the rest of your code follows

            if action == 'defend':
                print(" ")
                self.player_character.defend()  # Boost defense.            
                time.sleep(0.8)

            elif action == "attack":
                print(" ")
                self.player_character.attack(self.enemy)
                time.sleep(0.8)
                print(" ")

            elif action == "special attack":
                print(" ")
                spec_attack_attack_success = self.player_character.spec_attack(self.enemy)  
                if spec_attack_attack_success: # if special attack was successful
                    time.sleep(0.8)
                    print(" ")
                else:
                    print(" ")
                    action = "" # reset action to loop input
                    time.sleep(0.8)  
                    print(" ")

            elif action == "charge":
                print(" ")
                self.player_character.charge()
                time.sleep(0.8)

            elif action == 'heal':
                print(" ")
                if self.player_character.get_num_bandages(): # checks if get_num_banadages == true
                    self.player_character.heal()
                else:
                    self.player_character.heal() # The heal method will handle the absence of bandages
                    print(" ")
                    action = ""
                    time.sleep(0.8)                             
            else:
                print(" ")
                print('Invalid action!')
                self.turn_counter -= 1
                print(" ")
                action = ""  # reset the action, forcing the inner loop to repeat
                time.sleep(0.8)
   

    def charged_enemy_turn(self):
        pass # need to figure this out. on second thought i dont think i want enemies to charge. maybe only the boss. 
 
    def enemy_turn(self):
        print ("-----Enemy turn-----")
        print(" ")
        if self.enemy.is_hurt == True:
            self.enemy.enemy_is_hurt()
            if self.enemy.hp <= 0:
                    raise FightOverException  # enemy is defeated, break the fight loop
        
        if self.enemy.hp <= 0:
            raise FightOverException  # enemy is defeated, break the main fight loop
        

        if self.enemy.hp > 10:
        # High hp - if enemy has enough ap it performs a normal attack unless a random 1 in 4 condition is met for performing a special attack.
            if self.enemy.ap > 0:   
                if random.randint(1, 4) == 4:
                    self.enemy.spec_attack(self.player_character)
                else:
                    self.enemy.attack(self.player_character)
            else:
                    self.enemy.attack(self.player_character) 
        
        elif self.enemy.hp <= 10:
            
        # Low hp - if the enemy has enough ap it will perform a normal attack, heal, or special attack based on different random conditions.
            
            if self.enemy.ap > 0:
                random_number = random.randint(1, 3)
                if random_number == 1:
                    self.enemy.spec_attack(self.player_character)
                    if self.player_character.hp <= 0:
                        raise FightOverException
                elif random_number == 2:
                    self.enemy.attack(self.player_character)
                    if self.player_character.hp <= 0:
                        raise FightOverException
        
                else:
                    self.enemy.heal()
            else:
                random_number = random.randint(1, 2)
                if random_number == 1:
                    self.enemy.attack(self.player_character)
                  
                else:
                    self.enemy.heal()  

        self.player_character.stop_defending()
            

    def xp_up(self):
        pass

class Fight1(Fight):    #Contains Start() and fight1_intro()
    def __init__(self, player_character, enemy):
        super().__init__(player_character, enemy)
        self.enemy = enemy
    def fight_intro(self):
        print(" ")
        #time.sleep(2)
        print("The challenger is struck by the sight of an enigmatic archer clad in green....")
        input()
        #time.sleep(3)
        
        print(f"He stood like a sentinel, his piercing gaze fixated on {self.player_character}....")   
        input()
        #time.sleep(3)
        
        print("The air pulsated with the weight of impending conflict.... ")
        input()
        #time.sleep(3)
        
        print(f"{self.player_character} was about to face not just a skilled archer, but the living embodiment of rebellion....")
        input()
        #time.sleep(3)
        
        print(f"{self.enemy} has entered the arena....")
        input()
        #time.sleep(3)
        print(" ")
        print("FIGHT!")
        print(" ")
        

    def start(self):
        self.turn_counter = 0
        self.fight_intro()
        while player_character.hp > 0 and self.enemy.hp > 0:
            self.player_start()
                

    def xp_up(self):
        xp_gained = 100 - (self.turn_counter * 7)
        player_character.xp += xp_gained  # if player needs 72xp to reach level 2, 
        print (f"+ {xp_gained} XP")                     # meaning if more than 4 turns are taken in fight 1 player wont levl up. 
                                                       # 7 was used to keep numbers odd and even and not multiples of 10 for "realism"
                                                        # This could prove annoying later when calculating level up xp thresholds
        if player_character.xp >= 72:
            player_character.level_up()
            time.sleep(0.8)
            print(" ")            
        
class Fight2(Fight):    #Contains Start() and fight2_intro()
    def __init__(self, player_character, enemy):
        super().__init__(player_character, enemy)

    def fight_intro(self):
        time.sleep(0.8)
        print(" ")
        print(f"{self.enemy} has entered the arena!......")
        
        input()
        print("He's bloodied and bruised. He bounds towards you fists up, screaming 'Adriaaaaan!......'")
        
        input()
        print("FIGHT!.....")
        input()
        print("Rocky is in a rage and attacks first.....")
        print(" ")
        input()

    def start(self):
        self.turn_counter = 0
        self.fight_intro()
        while self.player_character.hp > 0 and self.enemy.hp > 0:
            self.enemy_start()

    def xp_up(self):
        xp_gained = 140 - (self.turn_counter * 7)
        player_character.xp += xp_gained # 4 tuns again so - 28 = 118, 118 + 72 = 190xp to level up.
        print (f"+ {xp_gained} XP")
        if player_character.level == 1:
            if player_character.xp >= 72:
                player_character.level_up()
                time.sleep(0.8)      
                print(" ")
        elif player_character.level == 2:
            if player_character.xp >= 190:
                time.sleep(0.8)
                player_character.level_up()            
            
class Fight3(Fight):    #Contains Start() and fight2_intro()
    def __init__(self, player_character, enemy):
        super().__init__(player_character, enemy)

    def fight_intro(self):
        time.sleep(0.8)
        print(" ")
        print("Rocky is down for the count when his coach rushes in from his corner.....")
        
        input()
        print("He fires a signal flare and within seconds a chopper is flying overhead.....")
        
        input()
        print("A whole crew rappel down and form a barrier around Rocky.....")
        
        input()
        print("The army crew disperse and a new, gloveless challenger rises to his feet wearing a red bandana.....")
        
        input()
        print(" 'To survive a war, you gotta become war.....' ")
        
        input()

        print(f"{self.enemy} has entered the arena!...")
        
        input()
                
        
    def start(self):
        self.turn_counter = 0
        self.fight_intro()
        while self.player_character.hp > 0 and self.enemy.hp > 0:
            self.enemy_start()

    def xp_up(self):
        xp_gained = 180 - (self.turn_counter * 7)
        player_character.xp += xp_gained 
        print (f"+ {xp_gained} XP")
        if player_character.level == 1:
            if player_character.xp >= 72:
                player_character.level_up()
                time.sleep(0.8)     
                print(" ")
        elif player_character.level == 2:
            if player_character.xp >= 190:
                time.sleep(0.8)
                player_character.level_up() 
        elif player_character.level == 3:
            if player_character.xp >= 335:  # 5 turns this time so - 180 - 35 = 145, 145 + 190 = 335 xp to level up.
                time.sleep(0.8)
                player_character.level_up()
    
class Fight4(Fight):    #Contains Start() and fight2_intro()
    def __init__(self, player_character, enemy):
        super().__init__(player_character, enemy)

    def fight_intro(self):
        print("")
       
        print("As the arena lights dim, a familiar silhouette emerges from the shadows.......")
        
        input()
        print("A legendary immortal warrior with centuries of battles etched into his very existence......")
        
        input()
        print("In one swift motion, he unsheathes his iconic sword, the unmistakable hum filling the arena.......")
        
        input()
        print("The quickening is about to begin, and the question lingers......")
        
        input()
        print(f"will {self.player_character} become the one to claim victory, or will they fall to the blade of the immortal? ")
        
        input()
        print("The stage is set, and there can be only one.....")
        
        print(f"{self.enemy} has entered the arena!...")
        
        input()
        print("FIGHT!....")
        input()
                
        
    def start(self):        # Player starts this time
        self.turn_counter = 0
        self.fight_intro()
        while self.player_character.hp > 0 and self.enemy.hp > 0:
            self.player_start()

    def xp_up(self):
        xp_gained = 220 - (self.turn_counter * 7)
        player_character.xp += xp_gained 
        print (f"+ {xp_gained} XP")
        print(" ")
        if player_character.level == 1:
            if player_character.xp >= 72:
                player_character.level_up()
                time.sleep(0.8)     
                print(" ")
        elif player_character.level == 2:
            if player_character.xp >= 190:
                time.sleep(0.8)
                print(" ")
                player_character.level_up() 
        elif player_character.level == 3:
            if player_character.xp >= 335:  # 5 turns this time so - 180 - 35 = 145, 145 + 190 = 335 xp to level up.
                time.sleep
                print(" ")(0.8)
                player_character.level_up()
        elif player_character.level == 4:
            if player_character.xp >= 420:  # 5 turns this time so - 220 - 35 = 185, 185 + 335 = 420 xp to level up.
                time.sleep(0.8)
                print(" ")
                player_character.level_up()

# TESTING

# Find Bandages
                        
'''player_character = Archer("TEST", 40, 5, 6, 6, 1, 3, 10)
player_character.find_bandages()
'''

# Level Up
'''
player_character = Archer("TEST", 40, 5, 6, 6, 1, 3, 10)
print ("level up?")
if input() == "yes":
   print(Human.level_up(player_character))
print ("level up?")
if input() == "yes":
   print(Human.level_up(player_character))
   print ("level up?")
if input() == "yes":
   print(Human.level_up(player_character))
'''




# define class instances

robin_hood = Archer("Robin Hood", 60, 1, 6, 15, 1, 1, 10)

rocky = Boxer("Rocky", 120, 2, 7, 15, 1, 5)

rambo = Gunner("Rambo", 180, 2, 10, 25, 1, 5, 10, 5) 

highlander = Warrior("Highlander", 250, 3, 12, 35, 1, 3)

teen_wolf = Monster("Teen Wolf", 280, 3, 15, 50, 1)

Terminator = Robo("Terminator", 350, 4, 20, 75, 1, 1, 100, 2)


# CALLING GAME LOGIC_________________________________________________

def create_character(): # this function print all the available classes and takes an input from a user to choose their class.
    
    print("")
    print("")
    print("")
    print("")
    print("Welcome to THE ARENA!....(Press ENTER to continue)")
    input()
    print("")
    print("Here you can pit your own fighter against the toughest fighters in history.....")
    input()
    print("")
    print("Choose your fighter!....")
    print(" ")
    input()
    print("Archer")
    base_archer_stats = Human.get_stats("Archer", 80, 3, 5, 7, 5)
    print(base_archer_stats)
    print(" ")
    time.sleep(0.5)
    print("Boxer")
    base_boxer_stats = Human.get_stats("Boxer", 70, 1, 8, 7, 4)
    print(base_boxer_stats)
    print(" ")
    time.sleep(0.5)
    print("Gunner")
    base_gunner_stats = Human.get_stats("Gunner", 65, 1, 8, 8, 4)
    print(base_gunner_stats)
    print(" ")
    time.sleep(0.5)
    print("Warrior")
    base_warrior_stats = Human.get_stats("Warrior", 70, 2, 6, 6, 3)
    print(base_warrior_stats)
    print(" ")
    time.sleep(0.5)
    print("Robot")
    base_robo_stats = Robo.get_stats("Robot", 80, 2, 7, 7, 2)
    print(base_robo_stats)
    print(" ")
    time.sleep(1)

    while True:
        print("Select a class by typing it's name:")    
    
        class_choice = input() # store user input in class choice variable
        print(" ")
        
        print("Enter a name for your character:") # user enters name and we store it in the name variable
        name = input()
        #time.sleep(0.8)
    
    # if class choice equls a particluar class type return that class type with name and base stats
        print(" ")
        if class_choice.lower() == "archer":
            time.sleep(1)
            print(f"{name} the Archer has entered the arena!")
            time.sleep(1)
            return Archer(name, 80, 3, 5, 7, 1, 5, 10)
            
        elif class_choice.lower() == "boxer":
            time.sleep(1)
            print(f"{name} the Boxer has entered the arena!")
            time.sleep(1)
            return Boxer(name, 70, 1, 8, 7, 1, 4)
            
        elif class_choice.lower() == "gunner":
            time.sleep(1)
            print(f"{name} the Gunner has entered the arena!")
            time.sleep(1)
            return Gunner(name, 65, 1, 8, 8, 1, 4, 25, 5)
            
        elif class_choice.lower() == "warrior":
            time.sleep(1)
            print(f"{name} the Warrior has entered the arena!")
            time.sleep(1)
            return Warrior(name, 70, 2, 6, 6, 1, 3)
            
        elif class_choice.lower() == "robot":
            time.sleep(1)
            print(f"{name} the robot has entered the arena!")
            time.sleep(1)
            return Robo(name, 80, 2, 7, 7, 1, 2, 100, 2)
        else:
            print("Invalid class, try again!")
            print("")
         

# Use the function to create a character
player_character = create_character()


# Fight 1. Robin Hood

fight1 = Fight1(player_character, robin_hood) # Pass player character instance and rovin hood instance into the fight 1 class
fight1.start()


# Fight over       
# Announcing result - now handled by fight over exception in start() function

player_character.reset_player_character()

# run xp up which will calculate xp gained and run level up if threshold is reached
fight1.xp_up()


# Fight 2. Rocky


fight2 = Fight2(player_character, rocky)
fight2.start()

player_character.reset_player_character()
fight2.xp_up()


# Fight 3. Rambo

fight3 = Fight3(player_character, rambo)
fight3.start()

player_character.reset_player_character()
fight3.xp_up()

player_character.find_bandages()  # player finds bandages after fight 3


#Fight 4. Highlander

fight4 = Fight4(player_character, highlander)
fight4.start()

player_character.reset_player_character()
fight4.xp_up()


