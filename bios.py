import re

class Deelnemer:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

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
        # if value1 == value4:
        #     print(name1, "great you already paid what you have to pay, \n")
        # elif value1 <= value4:
        #     v = value4 - value1
        #     print(name1, "you need to pay", "{0:.2f}".format(v) , "additionally, \n")
        # elif value1 >= value4:
        #     w = value1 - value4
        #     print(name1, "you wiil receive", "{0:.2f}".format(w) , "additionally, \n")
        # if value2 == value4:
        #     print(name2, "great you already paid what you have to pay, \n")
        # elif value2 <= value4:
        #     x = value4 - value2
        #     print(name2, "you need to pay", "{0:.2f}".format(x) , "additionally, \n")
        # elif value2 >= value4:
        #     y = value2 - value4
        #     print(name2, "you will receive", "{0:.2f}".format(y) , "additionally, \n")
        # if value3 == value4:
        #     print(name2, "great you already paid what you have to pay, \n")
        # elif value3 <= value4:
        #     z = value4 - value3
        #     print(name3, "you need to pay", "{0:.2f}".format(z) , "additionally, \n")
        # elif value3 >= value4:
        #     zz = value3 - value4
        #     print(name3, "you wiil receive", "{0:.2f}".format(zz) , "additionally, \n")
        pass

    def debug(self):
        for p in self.deelnemers:
            print( p.name + " : " + str(p.amount))

#
#
#
if __name__ == '__main__':
    biosBorrel = BiosBorrelCalculator()
    biosBorrel.collectNamesAndAmount()
    biosBorrel.debug()
