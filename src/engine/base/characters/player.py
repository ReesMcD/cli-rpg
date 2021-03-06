''' Playable Character Class '''
from .character import Character
from src.engine.base.characters.classes.playerclass import PlayerClass
from src.engine.core.database import Database

TABLE = "player"


class Player(Character):
    '''
    NPC or Non Playable Character is a character within the game that a player
    can interact with

    Attributes:
        name: String of the name of the character
        race: String of the race of the character
        class_name: String of the characters given player class
        inventory: Dictionary of a characters inventory
        level: Integer that denotes a character's level

    '''
    def __init__(
      self, name="", race="", class_name="", inventory=None, level=1):

        super().__init__(TABLE, name, race, class_name, inventory)
        self.level = level
        self.max_hitpoints = 0
        self.current_hitpoints = 0
        self.armor_class = 0
        self.stats = {}
        self.actions = {}
        self.abilites = {}
        self.hit_dice = 0
        self.map_location = (0, 0)
        self.building_location = (0, 0)
        self.xp = 0

        if class_name:
            self.__set_player_class(class_name)

    def print(self):
        print()
        print("------ {} ------".format(self.name))
        print("Race: {}".format(self.race))
        print("Level: {}".format(self.level))
        print("XP: {}".format(self.xp))
        print("Class: {}".format(self.class_name))
        print("HP: {}/{}".format(self.current_hitpoints, self.max_hitpoints))
        print("Armor Class: {}".format(self.armor_class))
        print("Stats: ")
        for key, value in self.stats.items():
            print(" {}:{}".format(key, value))
        print()

    def level_up(self):
        pass

    def move(self, direction: str):
        pass

    def __set_player_class(self, class_name):
        player_class = PlayerClass().get(class_name)
        self.max_hitpoints = player_class.hitpoints
        self.current_hitpoints = self.max_hitpoints
        self.armor_class = player_class.armor_class
        self.stats = player_class.stats
        self.actions = player_class.actions
        self.abilites = player_class.abilites
        self.hit_dice = player_class.hit_dice
