class Personne :
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    def affichage(self):
        print(f"le nom da la personne est {self.nom} , l'age est : {self.age}" )

p1 =  Personne("yasser",21)
p1.affichage()








































