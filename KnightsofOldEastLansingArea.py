#spartahack project: Knights of Old East Lansing
import random

class Player(object):
    def __init__(self,name):
        """Initiate variables to track the Player's Name, level, xp/requiredxptolevelup
        health/maxhealth, mana/maxmana, inventory, backpack.
        
        the inventory consists of 4 slots. slot 1 is for swords. slot 2 is for armor. slot 3 and 4 are for consumables."""
        self.name = name
        self.level = 0
        self.xp = 0
        self.requiredxp = 1000
        self.health = 100
        self.maxhealth = 100
        self.mana = 100
        self.maxmana = 100
        self.inventory = {1:"x",2:"x",3:"x",4:"x"}
        self.backpack = {}
        for n in range(1,10):
            self.backpack[n:"x"]
        
    def adjust_health(self,ammount):
        """change Player's health by ammount"""
        self.health += ammount
        
    def adjust_mana(self,ammount):
        """change Player's mana by ammount"""
        self.mana += ammount
    
    def improve_max_health(self,ammount):
        """increase Player's max health by ammount. hard capped at 500"""
        if self.maxhealth < 500:
            self.maxhealth += ammount
        
    def improve_max_mana(self,ammount):
        """increase Player's max mana by ammount. hard capped at 400"""
        self.maxmana += ammount
        
    def level_up(self):
        """increase Player's level by 1"""
        if self.level <125:
            self.level += 1
        self.xp = 0
        
    def add_xp(self,ammount):
        """increase the player's xp count by ammount. if enough to level up trigger level up"""
        self.xp += ammount
        if self.xp >= self.requiredxp:
            self.level_up()
            
    def equip(self,item,slot_number):
        """equip item into slot number slot_number"""
        self.inventory[slot_number] = item
        
    def unequip(self,slot_number):
        """takes item out of slot slot_number and puts it in the first empty spot in the backpack"""
        for n in range(1,10):
            if self.backpack[n] == "x":
                self.backpack[n] = self.inventory.pop([slot_number])

    def open_backpack_slot_check(self):
        """returns the number of open spots in the Player's backpack"""
        open_slot_count = 9
        for n in range(1,10):
            if self.backpack[n] != "x":
                open_slot_count -= 1
        return open_slot_count
    
    def open_inventory_slot_check(self):
        """returns the number of open slots in the Player's inventory"""
        open_slot_count = 4
        for n in range(1,5):
            if self.inventory[n] != "x":
                open_slot_count -= 1
        return open_slot_count
    
    def inventory_slot_open(self,slot_number):
        "checks if specific inventory slot is open returns True if it is False otherwise"
        if self.inventory[slot_number] == "x":
            return True
        else:
            return False
        
    def backpack_slot_open(self,slot_number):
        "checks if specific backpack slot is open returns True if it is False otherwise"
        if self.backpack[slot_number] == "x":
            return True
        else:
            return False
        
    def get_health(self):
        """return Player's current health"""
        return self.health
    
    def get_mana(self):
        """return Player's current health"""
        return self.mana
        
class Enemy(object):
    """"enemies have a name and health energy and power species and ability"""
    def __init__(self,name,health,energy,power,species,ability=None):
        self.name = name
        self.maxhealth = health
        self.health = health
        self.energy = energy
        self.power = power
        self.species = species
        
    def adjust_health(self,ammount):
        """change Enemy's health by ammount"""
        self.health += ammount
        
    def get_energy(self):
        """returns energy type"""
        return self.energy
    
    def get_health(self):
        """returns current health"""
        return self.health
    
    def get_power(self):
        return self.power
    
    def defeated(self,ratio):
        """returns an ammount of rewarded xp determined by an outside function"""
        return int(self.health * ratio)
    
    def __str__(self):
        return "{} {} {} {} {}".format(self.name,self.health,self.energy,self.power,self.species)

class Boss(Enemy):
    pass

class Room(object):
    """a cell in the floor"""
    def __init__(self,value,objects=None):
        self.occupancy = objects
        self.value = value
        enemy = Enemy("saskue",100,"arc",125,"ant")
        enemy2 = Boss("orichmaru",500,"arc",1250,"snake")
        chest1 = ["nothing"]
        player = Player("Kirito")
        town = ["elder","hospital","shope"]
        
    def claim_monster(self,monster=enemy):
        self.occupancy = monster
        self.value = "M"
        
    def claim_chest(self,chest=chest1):
        self.occupancy = chest
        self.value = "C"
        
    def claim_village(self,village=town):
        self.occupancy = village
        self.value = "V"
        
    def claim_boss_room(self,boss=enemy2):
        self.occupancy = boss
        self.value = "B"
        
    def __str__(self):
        return self.value

class Floor(object):
    def __init__(self):
        room = Room("?")
        self._cell = [[room for c in range(5)] \
                                for r in range(5)]
        self.revealed_dict = {}
        for c in range(5):
            for r in range(5):
                self.revealed_dict[c,r] = False
    
    def place_village(self,number,letter):
        """place a village at the given coordinates"""
        self._cell[number][letter].claim_village()
        
    def place_boss_room(self,number,letter):
        """place a boss room at the given coordinates"""
        self._cell[number][letter].claim_boss_room()
        
    def place_monster(self,number,letter,ammount=1):
        """place a monster/monsters in a room at the given coordinates"""
        self._cell[number][letter].claim_monster()
        if ammount > 1:
            self._cell[number][letter] = "m"
            
    def place_chest(self,number,letter):
        """place a chest in a room at the given coordinates"""
        self._cell[number][letter].claim_chest()
    
    def place_empty(self,number,letter):
        """place an empty spot on the map"""
        self._cell[number][letter] = "x"
        
    def cell_revealed(self,number,letter):
        """returns True if cell has been visted else otherwise"""
        return self.revealed_dict[(number,letter)]
    
    def reveal_cell(self,number,letter):
        """turns the reveal state of a cell to True"""
        self.revealed_dict[(number,letter)] = True
        
    def print_dict(self):
        """for dev purposes. literally just so i can copy the dict of coordinates"""
        print(self.revealed_dict.keys())
        
    def reveal_floor(self):
        for c in range(5):
            for r in range(5):
                self.reveal_cell(c,r)
        
    def cell_not_none_check(self,number,letter):
        """returns true if the cell is not none, false otherwise"""
        if self._cell[number][letter] == None:
            return False
        else:
            return True
        
    def get_cell(self,number,letter):
        """returns the value of a specific cell"""
        return self._cell[number][letter]
    
    def __str__(self):
        vline = '\n' + (' ' * 2) + ('+---' * 5) + '+' + '\n'
        numline = ' '.join([(' ' + str(i) + ' ') \
                            for i in range(1, 5 + 1)])
        str_ = (' ' * 3) + numline + vline
        for r in range(0, 5):
            str_ += chr(97 + r) + ' |'
            for c in range(0,5):
                if self.cell_revealed(c,r) and self.cell_not_none_check(c,r):
                    value = self.get_cell(c,r)
                else:
                    value = "?"
                str_ += " " + value + ' |'
            str_ += vline
        return str_
    
def create_random_floor(floor_number):
    floor = Floor()
    options = ["M","M","M","M","C","C","x","x","x","x"]
    floorplan_list = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    count = 0
    for coordinate in range(25):
        selected = floorplan_list.pop(random.randint(0,len(floorplan_list)-1))
        if count == 0:
            floor.place_village(selected[0],selected[1])
            count += 1
        elif count == 1:
            floor.place_boss_room(selected[0],selected[1])
            count += 1
        else:
            option = options[random.randint(0,9)]
            if option == "M":
                floor.place_monster(selected[0],selected[1])
            if option == "C":
                floor.place_chest(selected[0],selected[1])
            else:
                floor.place_empty(selected[0],selected[1])
    return floor
    
