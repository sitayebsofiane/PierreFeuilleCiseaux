from gamer import *
from game import *
name=input("welcome to the game Chifoumi, please enter your name: ")

gamer= Gamer(name)
pc= Pc()
print(Game.part_with_pc(gamer,pc))
