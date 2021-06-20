# Oppgave 2 
# Importerer Sang slik at denne klassen kan brukes her
from sang import Sang

# Definererer klassen spilleliste med listenavn som instansvariable 
class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

# Lager instansmetode som kan lese inn filer og legge elementer inn i _sanger, passer paa
# at split gjennomfoeres ved ;, slik at listen blir riktig 
    def lesFraFil(self, filnavn): 
        fil = open(filnavn)
        for linje in fil:
            alleData = linje.strip().split(';')
            self._sanger.append(Sang(alleData[0], alleData[1]))
        fil.close()

# Instansmetode som spiller av alle sangene i listen, dette gaar da tilbake til spill metoden fra forrige
# oppgave 
    def spillAlle(self):  
        for sang in self._sanger:
            sang.spill()

# Instansmetode som legger til en ny sang til listen 
    def leggTilSang(self, nySang):  
        self._sanger.append(nySang)

# Instansmetode som fjerner sang fra liste 
    def fjernSang(self, sang):  
        self._sanger.remove(sang)

# Instansmetode som bare spiller en sang om gangen, igjen bruker metode fra forrige oppgave 
    def spillSang(self, sang): 
        sang.spill()

# Instansmetode som gaar gjennom alle sangene og vil returnere ut den foerste sangen som er lik basert
# paa tittlene. Igjen bruker metode fra siste oppgave 
    def finnSang(self, tittel):  
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang

# Instansmetode som finner alle sanger fra samme artist og saa returnerer det en liste over disse sangene. 
    def hentArtistUtvalg(self, artistnavn):  # finner alle sanger med samme artist, returnerer liste
        utvalg = []
        for sang in self._sanger:
        # Hvis sangen har deler av av gitt artistnavn som artist saa vil sangen legges til utvalg listen 
            if sang.sjekkArtist(artistnavn):
                utvalg.append(sang) 
        return utvalg