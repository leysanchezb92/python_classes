class Weapon:
    def __init__(self, weapon_name, weapon_power):
        self.weapon_name = weapon_name
        self.weapon_power = weapon_power

    def attack(self):
        print(f"Attacking with {self.weapon_name} having power {self.weapon_power}")

class Character():
    def __init__(self, name, level, live, weapon:Weapon):
        self.name = name
        self._level = level
        self._live = live
        self.weapon = weapon

    @property # Getter method level
    def level(self):
        return self._level

    @level.setter #Setter method level
    def level(self, value):
        if self._level == 1 and value == 0:
            print(f"Player {self.name} is a starter")
        elif value <= self._level:
            print(f"Player {self.name} can't decrease level")
        else:
            increase = value - self._level
            self._level = value
            print(f"Player {self.name} has leveled up {increase} levels")


    @property # Getter method live
    def live(self):
        return self._live

    @live.setter # Setter method live
    def live(self, value):
        if value <= 0:
            self._live = 0
            print(f"Player {self.name} is dead")
        else:
            self._live = value

    def damage(self,amount):
        self._live -= amount
        print(f"{self.name} has taken damage!. Current health: {self.live}")

    def healing(self,amount):
        self._live += amount
        print(f"{self.name} has been healed!. Current health: {self.live}")
       

class Enemy(Character):
    def __init__(self, name, level, live, type_enemy, weapon:Weapon):
        super().__init__(name, level, live, weapon)
        self.type_enemy = type_enemy
    
    def attack(self):
        print(f"Enemy {self.name} attacks with {self.weapon.weapon_name} having power {self.weapon.weapon_power}")
        print("----------")
        print(f"Enemy has taken damage!. Current health: {self.live}")


class Allied(Character):
    def __init__(self, name, level, live, type_ally, weapon:Weapon):
        super().__init__(name, level, live, weapon)
        self.type_ally = type_ally
    
    def attack(self):
        print(f"Allied {self.name} attacks with {self.weapon.weapon_name} having power {self.weapon.weapon_power}")
        print("----------")
        print(f"Allied has taken damage!. Current health: {self.live}")

characters = []

def register_character(characters=characters):
    print("Register Character: ")

    character_type = input("What kind of character you want? (Allied or Enemy): ").strip().capitalize()
    name_character = input("what name you want for your character?: ").strip().capitalize()
    level = 1
    live = 100
    weapon_power = 10
    if character_type == "Enemy":
        enemy_weapon = Weapon('knife', weapon_power)
        enemy = Enemy(name_character, level, live, "Zombie", enemy_weapon)
        print(f"Enemy character '{name_character}' created successfully!")
        print("---- Character Details ----")
        print(f"Name: {enemy.name}")
        print(f"Weapon Name: {enemy.weapon.weapon_name}")
        print(f"Weapon Power: {enemy.weapon.weapon_power}")
        print(f"Type: {enemy.type_enemy}")

        characters.append(enemy)

    elif character_type == "Allied":
        allied_weapon = Weapon("sword", weapon_power)
        allied = Allied(name_character, level, live, "Knight", allied_weapon)
        print(f"Allied character '{name_character}' created successfully!")
        print("---- Character Details ----")
        print(f"Name: {allied.name}")
        print(f"Weapon Name: {allied.weapon.weapon_name}")
        print(f"Weapon Power: {allied.weapon.weapon_power}")
        print(f"Type: {allied.type_ally}")

        characters.append(allied)
    else:
        print("Invalid character type. Please choose 'Allied' or 'Enemy'.")

def attack_character():
    target = input("Enter the name of the character to attack: ").capitalize().strip()

    # Find the target character in the game
    for character in characters:    
        if character.name == target:
            character.damage(10)  # Example damage value
            weapon_attack = character.weapon.attack()
            print(f"Character {target} attacked successfully, dealing {weapon_attack} damage. Character's current health: {character.live}")
            print("------------------------")
            print("\n")
        elif character.live <= 0:
            print(f"Character {target} is already dead.")
        elif character.name != target:
            print(f"Character '{target}' not found.")

def heal_character():
    target = input("Enter the name of the character to heal: ").capitalize().strip()

    # Find the target character in the game
    for character in characters:    
        if character.name == target:
            character.healing(10)  # Example healing value
            print(f"Character {target} healed successfully. Character's current health: {character.live}")
            print("------------------------")
            print("\n")
        elif character.live <= 0:
            print(f"Character {target} is dead and cannot be healed.")
        elif character.name != target:
            print(f"Character '{target}' not found.")

def level_up_character():
    target = input("Enter the name of the character to level up: ").capitalize().strip()
    for character in characters:
        if character.name == target:
            character.level += 1
            print(f"Character '{target}' leveled up to level {character.level}!")
            return
    print(f"Character '{target}' not found.")

def show_all_characters(characters=characters):
    if not characters:
        print("No characters registered.")
        return
    print("---- All Characters ----")
    for character in characters:
        if isinstance(character, Enemy):
            specific_type = character.type_enemy
        elif isinstance(character, Allied):
            specific_type = character.type_ally
        print(f"Name: {character.name}, Type: {specific_type}, Level: {character.level}, Health: {character.live}, Weapon: {character.weapon.weapon_name}, Power: {character.weapon.weapon_power}")
        print("------------------------")
        print("\n")

def mostrar_menu():
    print(" ------------ MINIGAME------------- ")
    print(" 1. Register your Character")
    print(" 2. Attack Allied/Enemy")
    print(" 3. Heal Allied/Enemy")
    print(" 4. Level up Allied/Enemy")
    print(" 5. Show all characters")
    print(" 0. Salir")

def main():
  #Funcion principal
  while True:
    mostrar_menu()
    opcion = input("Ingrese la opcion de 0 a 7: ").strip()
    
    if opcion == "1":
      register_character()
    elif opcion == "2":
      attack_character()
    elif opcion == "3":
        heal_character()
    elif opcion == "4":
        level_up_character()
    elif opcion == "5":
      show_all_characters()
    elif opcion == "0":
      print("Session ended, goodbye!")
      break

if __name__ == "__main__":    
    main()


