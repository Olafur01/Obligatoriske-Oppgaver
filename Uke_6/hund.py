# Oppgave 3
# Oppgave 3.1 
# # Definerer klassen først, før oppretter konstruktøren og så initaliserer instansvariabelene. Samme fremgangs-
# måte som i tidligere oppgaver brukes her i henhold til instansmetoder. 
class Hund:
    def __init__(self, alder, vekt, metthet = 10):
        self.alder = alder
        self.vekt = vekt 
        self.metthet = metthet

# Oppgave 3.2 
# Lager to instansmetoder for å hente alder og hente vekt. 
    def hentAlder(self):
        return self.alder
    
    def hentVekt(self):
        return self.vekt

# Oppgave 3.3  
# Lager en instansmetode, der hvis en hund springer, så blir metthet redusert med en og hvis den  
    def spring(self):
        self.metthet -= 1
        if self.metthet < 5:
            self.vekt -= 1 
        return self.metthet, self.vekt

# Oppgave 3.4
# Lager en instansmetode der hunden spiser hvor da metthet økes, og at den kan øke med mengde. En if statement 
# blir også laget som øker vekt hvis metthet er større enn 7 
    def spis(self, mengde):
        self.metthet += mengde
        if self.metthet > 7:
            self.vekt += 1 
        return self.metthet, self.vekt 

