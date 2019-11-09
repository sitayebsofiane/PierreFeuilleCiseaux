class Game:
    def part(self,gamer1,gamer2):
        while gamer1.score<3 and gamer2.score<3:
            res_gamer1=gamer1.play()
            res_gamer2=gamer2.play()   
            if res_gamer1=="feuille" and res_gamer2=="pierre":
                    gamer1.score+=1
            elif res_gamer1=="pierre" and res_gamer2=="ciseaux":
                    gamer1.score+=1
            elif  res_gamer1=="pierre" and res_gamer2=="ciseaux":
                    gamer1.score+=1              
            elif res_gamer1 != res_gamer2:
                gamer2.score+=1
        if gamer1.score==3:
            return gamer1.name+" win"
        elif gamer2.score==3:
            return gamer2.name+" win"

