import random
#creaing  the main character
class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class


def cave_event():
    print("You find a treasure chest!")
    action = input("Do you want to (open, leave): ").lower()
    if action == "open":
        print("You found gold coins!")
    elif action == "leave":
        print("You leave the chest untouched.")
    else:
        print("Invalid action.")


def castle_event():
    print("You meet a mysterious stranger.")
    action = input("Do you want to (talk, ignore): ").lower()
    if action == "talk":
        print("The stranger gives you a quest!")
    elif action == "ignore":
        print("You ignore the stranger and move on.")
    else:
        print("Invalid action.")


def forest_event():
    print("You encounter a wild beast!")
    action = input("Do you want to (fight, flee): ").lower()
    if action == "fight":
        print("You bravely fight the beast and win!")
    elif action == "flee":
        print("You successfully escape the beast.")
    else:
        print("Invalid action.")


class Game:
    def __init__(self):
        self.player = None
        self.current_location = "village"

    def create_character(self):
        name = input("Enter your character's name: ")
        character_class = input("Choose your class (Warrior, Mage, Thief): ")
        self.player = Character(name, character_class)
        print(f"Character {self.player.name} created as a {self.player.character_class}.")

    def start_game(self):
        print("Welcome to the Adventure Game!")
        self.create_character()
        self.main_loop()

    def main_loop(self):
        while True:
            action = input("What would you like to do? (explore, quit): ").lower()
            if action == "explore":
                self.explore()
            elif action == "quit":
                print("Thank you for playing!")
                break
            else:
                print("Invalid action. Please try again.")

    def explore(self):
        locations = ["forest", "cave", "castle"]
        self.current_location = random.choice(locations)
        print(f"You explore the {self.current_location}.")
        if self.current_location == "forest":
            forest_event()
        elif self.current_location == "cave":
            cave_event()
        elif self.current_location == "castle":
            castle_event()


if __name__ == "__main__":
    game = Game()
    game.start_game()