class Gamer:
    #constructor joueur
    def __init__(self,name):
        self._setname(name)
        self.score=0
    #setter
    def _setname(self,new_name):
        import re
        # i check his name should be alphabitique min=2 and max=10 else i will take name Player1
        if  re.search(r"^[A-Za-z\-._]{2,10}$",new_name) is None :
            self._name="Player1"
        else:
            self._name=new_name
    #getter
    def _getname(self):
        return self._name
    #methode of humain gamer
    def play(self):
        import re
        while 1:
            respense=input("veillez entrez pierre,feuille ou ciseaux :").lower()
            if re.search(r"^p[ierre]", respense) :
                print(self._getname()+" a chosie pierre avec score {} ".format(str(self.score)))
                return "pierre"
            elif  re.search(r"^f[euille]", respense):
                print(self._getname()+" a chosie feuille avec score {}".format(str(self.score)))
                return "feuille"
            elif  re.search(r"^c[iseaux]", respense):
                print(self._getname()+" a chosie ciseaux avec score {}".format(str(self.score)))
                return "ciseaux"
    #encapsulation of name gamer
    name=property(_getname,_setname)
#class  Pc extends Gammer
class Pc(Gamer):
    def __init__(self):
        Gamer.__init__(self,"computer")
    #method of computer gamer
    def play(self):
        import random
        choices=["pierre","feuille","ciseaux"]
        choice=choices[random.randint(0,2)]
        print(self._getname()+" a choisie "+choice+" avec un  score "+str(self.score))
        return choice

