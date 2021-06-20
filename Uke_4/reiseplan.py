# Oppgave 3.1
# For at bruker skal fylle listen steder med fem reisemål, så bruker jeg range funksjonen med (5), slik at 
# denne løkken blir kjørt fem ganger. Jeg tar så å legge til tekstrengene som bruker skriver in, og konverter
# med .title() funksjonen, slik at det blir lettere å sammenligne senere. Kunne også brukt capitalize, lower, 
# eller upper for samme effekt. 
steder = []
for i in range(5):
    i = input("Skriv inn et reisemaal: ")
    steder.append(i.title())
print(steder)

# Oppgave 3.2
# Bruker samme logikk her som i siste deloppgave, bare at jeg bruker .lower funksjonen isteden. Grunnen for 
# at jeg brukte title() på forrige er fordi det er land, og når det skrives ut senere så ser dette finere ut 
klesplagg = []
for i in range(5):
    i = input("Skriv inn et klesplagg du vil ha med paa turen: ")
    klesplagg.append(i.lower())
print(klesplagg)

# Her legger jeg også inn instrukser om hvordan jeg vil at bruker skal inputte verdiene, blir mer oversiktelig
avreisedatoer = []
for i in range(5):
    i = input("Skriv in hvilken dato du vil reise til din destinasjon (eksempel 21.01.2020): ")
    avreisedatoer.append(i)
print(avreisedatoer)


# Oppgave 3.3
# Lager en nøstet liste ved å bare legge hver av listene jeg har laget inn i en liste. Hvis jeg hadde "summert"
# listene, ved bruk av pluss tegn, så hadde jeg bare laget en stor liste, men jeg ville ha nøstete lister isteden. 
reiseplan = [steder, klesplagg, avreisedatoer]

# Oppgave 3.4
# For at jeg skal printe ut alle reisemålene slik at de kommer på hver sin linje og uten at det ser ut som
# en liste med [] rundt de, for så å bruke join funksjonen for å trekke de ut av listen, for så å bruke map
# funksjonen for å iterate over hver liste i listen min.   
for liste in reiseplan:
    print(', '.join(map(str, liste)))

# Oppgave 3.5
# Her lager jeg en end statement, som brukeren må skrive slutt inn i hvis de vil avslutte programmet. 
# Jeg bruker deretter nøstete løkker for å få forskjellig input fra brukeren. Først så vil jeg at brukeren
# skal velge listen de er interessert å se på, som må være mellom 0 - 2, ellers får de tilbake at det er en 
# ugyldig input. Denne loopen avsluttes først når variabelen i1 er enten 0, 1, eller 2. Det samme skjer da med
# valg av element i i2, bare at det er et tall fra 0 - 4 som må velges for å se et element. Når disse variabelene 
# er valgt så printes det til terminalen. Bruker blir deretter spurt om de vil avslutte, ved å skrive slutt. hvis 
# de ikke gjør dette blir hele loopen kjørt på nytt. 
end_statement = ''
while end_statement != 'slutt':
    i1 = 100
    while i1 > 2 or i1 < 0: 
        i1 = int(input("Hvilken liste vil du se paa? (steder = 0, klesplagg = 1, avreisedato = 2) "))
        if i1 > 2 or i1 < 0:
            print("Ugyldig input!")
    i2 = 100
    while i2 > 4 or i2 < 0: 
        i2 = int(input("Hvilket element listen du har valgt vil du se paa? (0-4) "))
        if i2 > 4 or i2 < 0: 
            print("Ugyldig input!")
    print(reiseplan[i1][i2])
    end_statement = (input("For å avslutte programmet skriv 'slutt'. Hvis du vil se paa noe annet ved reisemaal skriv noe annet. ")).lower()







    
