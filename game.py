class Game:
    def part_with_pc(gamer1,gamer2):
        while  gamer1.score<3 and  gamer2.score<3:
            if gamer1.play()=="feuille" and gamer2.play()=="pierre":
                gamer1.score+=1
            elif gamer1.play()=="pierre" and gamer2.play()=="ciseaux":
                gamer1.score+=1
            elif  gamer1.play()=="pierre" and gamer2.play()=="ciseaux":
                gamer1.score+=1              
            elif gamer1.play() != gamer2.play():
                gamer2.score+=1

        if gamer1.score==3:
            return gamer1.name+" is win"
        elif gamer2.scor==3:
            return gamer2.name+" is win"
                  
    part_with_pc=staticmethod(part_with_pc)
