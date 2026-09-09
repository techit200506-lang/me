class Personne :
    def afficher(self):
        print("personne")

class Etudiant(Personne):
    def afficher(self):
        print("Etudiant")


class Prof(Personne):
    def afficher(self):
        print("Prof")


t = [Personne(),Etudiant(),Prof()]

for x in t :
    x.afficher()