# Oppgave 4.1
# Definerer klassen først, før oppretter konstruktøren og så initaliserer instansvariabelene
class Dato:
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self.nyDag = nyDag
        self.nyMaaned = nyMaaned
        self.nyttAar = nyttAar

    # Oppgave 4.2 a)
    # Ettersom jeg skal lese av året for datoen så printes ved bruk av f formatet for strenger
    def lesAar(self):
        print(f"Aaret som er skrevet inn er {self.nyttAar}")

    # b)
    # Når jeg printer ut datoen bruker jeg dd.mm.yyyy formatet
    def skriv_ut_datoen(self):
        print(f"{self.nyDag}.{self.nyMaaned}.{self.nyttAar}")

    # c)
    # For å sjekke en dato 
    def sjekk_dag(self, dato):
        if dato == self.skriv_ut_datoen():
            return True 

            
        
