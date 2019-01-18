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
    def __init__(self, van, naar, bedrag):
        self.van = van
        self.naar = naar
        self.bedrag = bedrag
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

        # Maak nieuw leeg kasboek
        self.kasboek = Kasboek()

        # Bereken totaal gespendeerd
        for deelnemer in self.deelnemers:
            self.kasboek.totaal += deelnemer.amount

        # Copy deelnemers in locale var dn: algoritme is destructief
        dn = []
        for idx in self.deelnemers:
            if abs((idx.amount * len(self.deelnemers)) - self.kasboek.totaal) >= 0.001:
                dn.append(idx)

        # Voor alle deelnemens behalve jezelf bereken evt. betaling
        for idx in dn:
            for idy in dn:
                if idx != idy:
                    betaling = (idx.amount / len(dn)) - (idy.amount / len(dn))
                    if betaling > 0:
                        kasboekRegel = KasboekRegel(idy.name, idx.name, betaling)
                        self.kasboek.items.append(kasboekRegel)

    #
    #
    def printOutput(self):
        print('--------------------------------------------------------------')
        print('In totaal is verbrast: ', "{0:.2f}".format(self.kasboek.totaal))
        for k in self.kasboek.items:
             print(k.naar, " krijgt van ", k.van, "{0:.2f}".format(k.bedrag) + " Euro")

#
#
#
if __name__ == '__main__':
    biosBorrel = BiosBorrelCalculator()
    biosBorrel.collectNamesAndAmount()
    biosBorrel.calculate()
    biosBorrel.printOutput()
