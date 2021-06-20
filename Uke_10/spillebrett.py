from random import randint
from celle import Celle

class Spillebrett:
    # 1 Oppretter konstruktøren for spillbrettet, med rader og kolonner som parametere
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        # Etablerer variable for generasjoner og rutenett
        self._generasjon = 0
        self._rutenett = []
        
        # Oppretter et rutenett ved bruk av en nøstet løkke. Denne lager da en to 
        # dimensjonell liste og populerer den med objekter. Bruker klassen celle for å
        # etablere disse objektene. 
        for antall_rader in range(self._rader):
            rad = []
            for antall_kolonner in range(self._kolonner):
                ny_celle = Celle()
                rad.append(ny_celle)
            self._rutenett.append(rad)

        # 2b)
        # Denne variabelen setter statusen for celler 
        self._generer()

    # 2 
    # Instansemetode som sørger for at en tredjedel av cellene blir satt som levende 
    # Bruker en nøstet løkke for a sette randomtall for hver celle
    def _generer(self):
       for rad in range(len(self._rutenett)):
           for kolonne in range(len(self._rutenett[0])):
               et_random_tall = randint(0,2)
               # Hvis det randomiserte tall er lik 1, så vil cellen bli levende 
               if et_random_tall == 1:
                   self._rutenett[rad][kolonne].settLevende()

    # 3
    # Oppretter en instansmetode som skriver ut spillbrettet
    def tegnBrett(self):
        # Passer på å toemme terminalviduet 
        for i in range(10):
            print()
        # Oppretter brettet ved bruk av en nøstet løkke
        for rad in range(len(self._rutenett)):
            print()
            for kolonne in range(len(self._rutenett[0])):
                print(self._rutenett[rad][kolonne].hentStatusTegn(), end = " ")
        print()

    # 4
    # Instansmetode som tar inn korrdinatene til en celle, og returnerer en liste med naboer, 
    # med parameterne rad og kolonne
    def finnNabo(self, rad, kolonne):
        naboer = []

        # Oppretter en funksjon ettersom en skal sjekke naboer 360 grader, og dette
        # forenkler prosessen litt 
        def sjekk(rad, kolonne):
            if rad >=0 and rad <= len(self._rutenett)-1 and kolonne >=0 and kolonne<=len(self._rutenett[0])-1:
                naboer.append(self._rutenett[rad][kolonne])

        # Sjekker nord
        sjekk(rad-1,kolonne) 
        # Sjekker nordøst 
        sjekk(rad-1,kolonne+1) 
        # Sjekker øst 
        sjekk(rad,kolonne+1)  
        # Sjekker sørøst 
        sjekk(rad+1,kolonne+1)
        # Sjekker sør
        sjekk(rad+1,kolonne)  
        # Sjekker sørvest
        sjekk(rad+1,kolonne-1)  
        # Sjekker vest
        sjekk(rad,kolonne-1)
        # Sjekker nordvest
        sjekk(rad-1,kolonne-1) 
    
        return naboer

    # 5
    # Oppretter en instansmetode som sjekker om en celle skal drepes eller gjenopplives
    def oppdatering(self):
        gjennopplive = []
        drep = []
        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[0])):
        # Her vil vi prøve å finne antall levende og døde naboer for hver celle. Ut
        # i fra dette skal vi se hva som kommer til å skje med hver enkelt celle 
                cellen = self._rutenett[rad][kolonne]
                levende_naboer = 0 
                doede_naboer = 0
                # Bruker en løkke for å sjekke naboer 
                for nabo in self.finnNabo(rad, kolonne):
                    if nabo.erLevende():
                        levende_naboer += 1
                    else:
                        doede_naboer += 1 
                # En løkke som ser om en celle er levende, og hvis den er det samt enten 
                # har mindre enn to levende naboer eller mer enn tre levende naboer så blir 
                # den drept 
                if cellen.erLevende():
                    if levende_naboer < 2 or levende_naboer > 3:
                        drep.append(cellen)
                # En løkke hvor en ser om en død celle har 3 levende naboer. Hvis
                # dette er sant så blir den gjenopplivet 
                if cellen.erLevende() == False:
                    if levende_naboer == 3:
                        gjennopplive.append(cellen)
        
        # Setter celler i gjennopplive listen til levende, mens celler i drep listen 
        # til død
        for celle in gjennopplive:
            celle.settLevende()
        for celle in drep:
            celle.settDoed()
        self._generasjon += 1


    # 6
    # Instansmetode som sjekker for hver enkelt celle om den er levende eller død 
    def finnAntallLevende(self):
        antall_levende = 0
        # Bruker en nøstet for løkke for å gå gjennom hver enkel celle for å 
        # sjekke statusen for hver enkel celle
        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[0])):
                cellen = self._rutenett[rad][kolonne]
                if cellen.erLevende():
                    antall_levende += 1
        return antall_levende 
    
    # Definerer en siste instansmetode som skriver ut setning med info om generasjon 
    # og antall levende celler
    def skrivInfo(self):
        print(f"Generasjon {self._generasjon} - antall levende celler: {self.finnAntallLevende()}")