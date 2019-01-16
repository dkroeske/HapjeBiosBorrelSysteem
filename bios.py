import re

class Deelnemer:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Kasboek:
    def __init__(self):
        self.totaal = 0
        self.items = []
        pass

class KasboekRegel:
    def __init__(self):
        self.van = 0
        self.naar = 0
        self.bedrag = 0
        pass

class BiosBorrelCalculator:

    # Initialisatie
    def __init__(self):
        pass

    # Verzamelen wie er allemaal meedoen en met welke inleg
    def collectNamesAndAmount(self):

        self.deelnemers = []

        for idx in range(3):
            name  = input("What's your name?\t")
            amount = float(input("Hi " + name + ", how much have you paid tonight (please use . for decimal)?\t"))

            # Test voor valid name and amount input.
            # Use regex: naam moet voldoen aan beginletter en min 3 characters
            if re.match(r"\w[a-zA-Z]{2,}$", name) and isinstance(amount, float)  :
                self.deelnemers.append( Deelnemer(name = name, amount = amount) )
            else:
                print("Ongeldige input, bye")
                exit()

    # Verzamelen wie er allemaal meedoen en met welke inleg
    def calculate(self):

        self.kasboek = Kasboek()

        #Bereken totaal gespendeerd
        for deelnemer in self.deelnemers:
            self.kasboek.totaal += deelnemer.amount

        # Voor alle deelnemens behalve jezelf
        for deelnemer in self.deelnemers:
            for idx in self.deelnemers:
                if deelnemer != idx:
                    betaling = (deelnemer.amount / 3) - (idx.amount / 3)
                    if betaling > 0:
                        print(deelnemer.name , " betaalverzoek aan ", idx.name, " voor ", "{0:.2f}".format(betaling) + " Euro" )

    def debug(self):
        for p in self.deelnemers:
            print( p.name + " : " + str(p.amount))

#
#
#
if __name__ == '__main__':
    biosBorrel = BiosBorrelCalculator()
    biosBorrel.collectNamesAndAmount()
    biosBorrel.calculate()
