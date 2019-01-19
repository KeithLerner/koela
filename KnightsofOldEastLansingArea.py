#spartahack project: player unnamed's adventure game

class Player(object):
    def __init__(self,name):
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
        
    