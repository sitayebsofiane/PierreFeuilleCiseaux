class Gamer:
    #constructor joueur
    def __init__(self,name):
        self._setname(name)
        self.score=0
    #setter
    def _setname(self,new_name):
        import re
        valide_expresion=r"[a-z]{2,10}[A-Z]{0,10}[ .-_]?"
        if not re.match(new_name,valide_expresion) :
            self._name=new_name
        else:
            self._name="Player1"
    #getter
    def _getname(self):
        return self._name
    #methode of
    def play(self):
            while 1:
                respense=input("veillez entrez pierre,feuille ou ciseaux :")
                if respense.lower() in ["pierre","feuille","ciseaux"]:
                    print(self._getname()+" chose "+respense+" wize score "+str(self.score))
                    return respense
    #encapsulation of name gamer
    name=property(_getname,_setname)
    
class Pc(Gamer):
    def __init__(self):
        Gamer.__init__(self,"computer")
    def play(self):
        import random
        choices=["pierre","feuille","ciseaux"]
        choice=choices[random.randint(0,2)]
        print(self._getname()+" chose "+choice+" wize score "+str(self.score))
        return choice

