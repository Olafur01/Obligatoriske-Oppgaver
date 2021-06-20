# Oppgave 1
# Oppgave 1.1 
# Definerer klassen først, før oppretter konstruktøren og så initaliserer instansvariabelene. For å opprettholde
# at objektene beholder sine verdier hele tiden, så brukes instansmetoder. Derfor inkluderes alltid self som 
# et parameter/argument. 
class Motorsykkel:
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self.merke = merke
        self.registreringsnummer = registreringsnummer
        self.kilometerstand = kilometerstand

# Oppgave 1.2
# Øker kilometeravstanden for så å returnere denne instansverdien, slik at den beholder denne økningen
    def kjor(self, km):
       self.kilometerstand += km
       return self.kilometerstand

# Oppgave 1.3 
# Returnerer kilometerstanden ved bruk av return funksjonen.
    def hentKilometerstand(self):
        return self.kilometerstand 

# Oppgave 1.4
# Bruker f string formen for å returnere alle instansvariabelene, samt kilometerstand hvis den har økt.
    def skrivUt(self):
        print(f'Bilens merke er {self.merke}, registreringsnummeret er {self.registreringsnummer}, og den har kjort {self.kilometerstand}')
