class Compte:
    def __init__(self, solde):
        self.__solde = solde

    def deposer(self, montant):
        self.__solde += montant

    def afficher_solde(self):
        print(self.__solde)



c1 = Compte(1000)

c1.deposer(500)


c1.afficher_solde()