class Joueur:
    #constructor joueur
    def __init__(self,name,score):
        self._setname(name)
        self.score=0
        print("creation {} avec le score {}".format(self._name,self.score))
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
    #encapsulation of name gamer
    name=property(_getname,_setname)
    
