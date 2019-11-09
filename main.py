from gamer import *
from game import *
name=input("welcome to the game Chifoumi, please enter your name: ")

gamer= Gamer(name)
pc= Pc()
print("welcome "+gamer.name+" you are palying wize "+pc.name)
game=Game()
print(game.part_with_pc(gamer,pc))
