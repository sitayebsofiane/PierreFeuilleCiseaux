class Joueur:
    #constructor joueur
    def __init__(self,name,score):
        self._name=name
        self._score=0
        print("creation {} avec le score {}".format(self._name,self._score))
    
    def _setnom(self,new_name):#setter
        import re
        valide_expresion=r"[a-ZA-Z]{2,30}[ .-_]"
        if not re.match(valide_expresion, new_name) :
            self._name="Player1"
        else:
            self._name=new_name

    
