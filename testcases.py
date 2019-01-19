#test cases for KOELA

from KnightsofOldEastLansingArea import Floor as Floor
from KnightsofOldEastLansingArea import Enemy as Enemy
from KnightsofOldEastLansingArea import Boss as Boss
from KnightsofOldEastLansingArea import create_random_floor as create_random_floor
from KnightsofOldEastLansingArea import Room as Room
from KnightsofOldEastLansingArea import create_player as create_player
from KnightsofOldEastLansingArea import create_goblin as create_goblin
from KnightsofOldEastLansingArea import create_dark_elf as create_dark_elf
from KnightsofOldEastLansingArea import create_spider as create_spider

def case1():
    print("Case 1: floor design and full reveal".upper())
    print()
    floor = Floor()
    print(floor)
    print("adding village at 3c")
    print()
    floor.place_village(2,2)
    floor.reveal_cell(2,2)
    print("adding boss room at 2a")
    print()
    floor.place_boss_room(1,0)
    floor.reveal_cell(1,0)
    print("adding 1 monster at 5b")
    print()
    floor.place_monster(3,1,1)
    floor.reveal_cell(3,1)
    print("adding 2 monsters at 5c")
    print("revealing board")
    print(floor)
    print()
    print()

#floor.print_dict()
def case2():
    print("case 2: enemy printing".upper())
    enemy = Enemy("EnEmY007",100,"ARC",25,"Ant")
    print("Enemy: {}".format(enemy))
    boss = Boss("BoSs001",150,"ARC",50,"Ant King")
    print("Boss: {}".format(boss))
    print()
    print()


def case3():
    print("case 3: random floor plan".upper())
    floor = create_random_floor(1)
    floor.reveal_floor()
    print(floor)
    print()
    print()


def case4():
    print("case 4: room class test".upper())
    print("this room is now filled with balloons")
    room=Room("balloons")
    print(room)
    room.claim_boss_room()
    print("this room is now a boss room")
    print(room)
    room.claim_village()
    print("this room is now a village room")
    print(room)
    room.claim_monster()
    print("this room is now a monster room with default monster")
    print(room)
    room.claim_chest()
    print("this room is now a chest room with a default chest")
    print(room)
    

def case5():
    """test player creation"""
    player = create_player("Gon Freeces")
    print(player)
    
def case6():
    """test goblin creation"""
    goblin = create_goblin()
    print(goblin)
    print("remoiving 25 health")
    goblin.adjust_health(-25)
    print(goblin)
    print("goblin has an attack power of {}".format(goblin.get_power()))
    print("goblin has an energy type of {}".format(goblin.get_energy()))
    print("goblin has health of {}".format(goblin.get_health()))
    print("goblin has species type of {}".format(goblin.get_species()))
    
def case7():
    """test dark elf creation"""
    elf = create_dark_elf()
    print(elf)
    print("remoiving 25 health")
    elf.adjust_health(-25)
    print(elf)
    print("dark elf has an attack power of {}".format(elf.get_power()))
    print("dark elf has an energy type of {}".format(elf.get_energy()))
    print("dark elf has health of {}".format(elf.get_health()))
    print("dark elf has species type of {}".format(elf.get_species()))
        
def case8():
    """test spider creation"""
    spider = create_spider()
    print(spider)
    print("remoiving 25 health")
    spider.adjust_health(-25)
    print(spider)
    print("spider has an attack power of {}".format(spider.get_power()))
    print("spider has an energy type of {}".format(spider.get_energy()))
    print("spider has health of {}".format(spider.get_health()))
    print("spider has species type of {}".format(spider.get_species()))    

case8()
