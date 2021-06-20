# Oppgave 1 
# Setter opp klassen sang med instansvariablene tittel og artist 
class Sang:
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    # Instansemetode som viser hvilken sang som spiller og hvem som synger den 
    def spill(self):  
        print(f"Spiller {self._tittel} av {self._artist}")

    # instansemetode som returnerer tittel
    def tittel(self):  
        return(self._tittel)

    # Instansemetode som sjekker om en del av et gitt navn er likt en del av navnet til artisten
    def sjekkArtist(self, navn):  # sjekker om en del av gitt navn er likt en del av artistnavn
        oppdeltArtist = self._artist.split()
        oppdeltNavn = navn.split()
        # Loekker gjennom navnet til artisen og hvis en del av artistnavn
        # vil True bli returnert  
        for i in oppdeltArtist:
            if i in oppdeltNavn: 
                return True

    # Instansemetode som sjekker om sang titlene er lik titelen oppgitt
    # Sammenligner tittel med self._tittel gjennom lower funksjonen og returer true eller false
    def sjekkTittel(self, tittel): 
        return tittel.lower() == self._tittel.lower()

    # Instansemetode som er en kombinasjon av sjekktittel og sjekkartist, returnerer true hvis 
    # parameterene som ble satt frem her oppfylles, ellers blir det false.
    def sjekkArtistOgTittel(self, artist, tittel): 
        oppdeltArtist = self._artist.split()
        oppdeltNavn = artist.split()
        for i in oppdeltArtist:
            if tittel.lower() == self._tittel.lower() and i in oppdeltNavn:
                return True
