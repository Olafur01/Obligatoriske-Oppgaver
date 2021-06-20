'''
Oppgavetekst:
Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter
og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
instansvariabel med en tom liste hobbyer. Skriv en metode leggTilHobby som tar
imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode
skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og
alder kaller på metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et
Person-objekt med informasjonen du får. Deretter skal brukeren ved hjelp av en
løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi
hobbyer skal statistikk om brukeren skrives ut.
'''

class Person:
    def __init__(self, navn, alder, hobby = []):
        self.navn = navn
        self.alder = alder
        self.hobby = hobby 

    def leggTilHobby(self, tekstStreng):
        self.hobby.append(tekstStreng)
        return self.hobby
    
    def skrivHobbyer(self):
        print(*self.hobby, sep=', ')
        return ', '.join(self.hobby)

    def skrivUt(self):
        print(f"Navnet ditt er {self.navn} og du er {self.alder} år gammel. Dine hobbier er {self.skrivHobbyer()}")

def hovedprogram():
    navn = input("Hva er navnet ditt? ")
    alder = input("Hvor gammel er du? ")
    person_1 =  Person(navn, alder)
    brukerinput = ''
    while brukerinput != 's':
        brukerinput = input("Skriv in 'i' for aa legge til en hobby, eller skriv 's' for å avslutte programmet ").lower() 
        if brukerinput == 'i':
            hobby = input("Skriv inn en hobby du har: ")
            person_1.leggTilHobby(hobby.title())
        elif brukerinput == 's':
            person_1.skrivUt()
        else:
            print("Ugyldig Input!")

hovedprogram()
