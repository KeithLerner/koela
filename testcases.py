#test cases for KOELA
from KnightsofOldEastLansingArea import Floor as Floor
from KnightsofOldEastLansingArea import Enemy as Enemy
from KnightsofOldEastLansingArea import Boss as Boss
from KnightsofOldEastLansingArea import create_random_floor as create_random_floor
from KnightsofOldEastLansingArea import Room as Room
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
    print("case 3: custom floor plan".upper())
    floor = create_random_floor(1)
    floor.reveal_floor()
    print(floor)
    print()
    print()


def case4():
    print("case 4: case 1 and case 2 combo")
    print
    
case3()