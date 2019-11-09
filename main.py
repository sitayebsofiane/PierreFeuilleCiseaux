from gamer import *
from game import *
while input("do you want to play Y or N: ").lower()!="n":
    name=input("welcome to the game Chifoumi, please enter your name: ")

    gamer= Gamer(name)
    pc= Pc()
    print("welcome "+gamer.name+" you are palying wize "+pc.name)
    game=Game()
    print(game.part(gamer,pc))
