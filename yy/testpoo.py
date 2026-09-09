class Personne :
    def __init__(self,nom,age):
        self.nom = nom 
        self.age = age
    def afficher(self):
        print(f" {self.nom}  {self.age}")


class Etudiant(Personne) :
    def __init__(self,nom,age,filiere,note):
        super().__init__(nom,age)
        self.filiere=filiere
        self._note = note
    def afficher(self):
        super().afficher()
        print(f" {self.filiere}  {self._note}")


class Professeur(Personne):
    def __init__(self,nom,age,matiere,salaire):
        super().__init__(nom,age)
        self.matiere = matiere
        self.__salaire=salaire
    def afficher(self):
            super().afficher()
            print(f" {self.matiere} {self.__salaire}")

class Directeur(Personne):
    def __init__(self,nom,age,bureau ,salaire):
        super().__init__(nom,age)
        self.bureau = bureau
        self.__salaire = salaire
    def afficher(self):
            super().afficher()
            print(f" {self.bureau} {self.__salaire}")


""""e1 = Etudiant("Yasser", 20, "Informatique", 17)

e1.afficher()"""

"""
p1 = Professeur("Mohammed", 56, "dev", "30000DH")
p1.afficher()"""

d1 = Directeur("Yasser", 50, "Bureau A", "40000DH")

d1.afficher()
