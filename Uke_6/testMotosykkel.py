# Oppgave 1.5
# For å få importert klassen så må vi importere den fra 
from Motorsykkel import Motorsykkel

def hovedprogram():
# Oppgave 1.6 
# Har fire parametere i konstrutøren, men ettersom den ene er self, så må jeg bare inputte tre, ellers 
# får man tilbake en feilmelding om for mange input parametere. 
    Motorsykkel_1 = Motorsykkel('Susuki', 'AA1234', 20000)
    Motorsykkel_2 = Motorsykkel('BMW', 'AD4534', 1000)
    Motorsykkel_3 = Motorsykkel('Susuki', 'DE2955', 523330)
    Motorsykkel_1.skrivUt()
    Motorsykkel_2.skrivUt()
    Motorsykkel_3.skrivUt()

# Oppgave 1.7
# Har to parametere instansmetoden, men ettersom den ene er self, så inputter jeg bare et argument. 
    Motorsykkel_3.kjor(10)
    print(Motorsykkel_3.hentKilometerstand())

# Oppgave 1.8
hovedprogram()