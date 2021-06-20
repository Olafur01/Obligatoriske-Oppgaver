# Oppgave 4.3 
from dato import Dato

def hovedprogram():
    # a)
    # Lager en ny objekt av Dato klassen 
    dato = Dato(15, 4, 2005)

    # b)
    print(dato.nyttAar)

    # c) 
    # Bruker en if, elif statement for sjekke om dagen er 15 eller 1 i måneden. 
    if dato.nyDag == 15:
        print("Loenningsdag!")
    elif dato.nyDag == 1:
        print("Ny maaned, nye muligheter!")

    # d)
    # Lager en ordbok for måneder slik at den senere kan brukes for å skrive ut en lesbar streng senere
    tabell_av_maaneder = {1: 'Januar',  2: "Februar", 3: "Mars", 4: "April", 5: "Mai", 6: "Juni", 7: "Juli", 8: "August", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
    streng_dato = f"{dato.nyDag} {tabell_av_maaneder[dato.nyMaaned]} {dato.nyttAar}"

    # e)
    print(streng_dato)

hovedprogram()
