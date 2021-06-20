# Oppgave 3 
# Oppgave 3.5
# Importerer Hund klasse før jeg lager et hovedprogram, og skaper et nytt objekt kalt Rex som gjennomfører
# springer to ganger og spiser 2 ganger. Vekten blir printet mellom hver gang. 
from hund import Hund

def hovedprogram():
    Rex = Hund(12, 20)
    Rex.spring()
    print(Rex.hentVekt())
    Rex.spring()
    print(Rex.hentVekt())
    Rex.spis(1)
    print(Rex.hentVekt())
    Rex.spis(1)
    print(Rex.hentVekt())

hovedprogram()

