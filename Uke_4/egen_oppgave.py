
'''I denne oppgaven skal du lage en bursdagsterminal, hvor en bruker har muligheten til å legge til 
så navn og korresponderende bursdager som de vil. Derfor må du inkludere en løkke som gir brukeren en slik mulighet
Isteden for å bruke en ordbok, vil jeg at du bruker lister. Når denne prossessen er ferdig så skal bruker 
ha mulighet til å skrive inn navnet til en vennog få en utskrift som tilsvarer "Bursdagen til "Olav" er den 
"24.08.1993. Hvis navnet ikke er i "terminalen" så skal dette meddeles med brukeren'''

 
def bursdagsterminalen():
    avslutt = ''
    navn = []
    bursdag = []
    

    while avslutt != 'slutt':

        # Lager en løkke her slik at hvis en person sitt navn allerede er i bursdagsterminalen så vil det ikke
        # være mulig å legge til et nytt med samme navn. Hvis det blir lagt til et nytt navn så vil løkken avslutte
        # ved bruk av en break statement. 
        while True:
            name = input("Velkomen til bursdagsterminalen. Vennligst skriv et navnet til en venn: ").title()
            if name in navn:
                print("Denne personen er allerede lagt til bursdagsterminalen")
            else:
                navn.append(name)
                break

        birthday = input("Skriv inn bursdagsdatoen til vennen din (eksempel 21.05.1999) ")
        bursdag.append(birthday)
        avslutt = input("Hvis du vil avslutte programmet, skriv in 'slutt'. ").lower()

    return navn, bursdag

navn, bursdag = bursdagsterminalen()

while True:
    query = input("Hvem vil du vite bursdagen til? " ).title()
    if query in navn:
        tall = navn.index(query)
        print("Bursdagen til {} er {}".format(query, bursdag[tall]))
        break
    else:
        print("Denne personen er ikke lagt til i bursdagsterminalen")
