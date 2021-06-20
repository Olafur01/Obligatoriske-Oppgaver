"""
For denne matplanen så lager jeg verdiene inn som en liste. Når jeg skal printe ut beboer navnene
bruker jeg .keys() funksjone, og bruker deretter .join og list for å gjøre dette om til en en gruppe av strings 
som kan skrives ut til terminalen. 
"""
matplan = {"Kari Nordmann":["omelett", "BLT", "fiskekaker i hvitsaus"], 
"Jens Stoltenberg":["havregrøt", "club sandwitch", "lasagne"], 
"Mette Marit":["full english breakfast", "caeser salat", "ramen nudler"]}


def matplanen():
    print("Beboerne: %s" % ", ".join(list(matplan.keys())))

    # Skaper en en variable som brukes til å ta brukeren sin input. Denne konvertes til en string gjennom str funksjonen 
    # Passer så på at unasett hvordan brukeren skrive inn navnet at det blir skrevet slik jeg vil at det skal se ut 
    # ved bruk at .title() funsksjonen. Denne gjøre første bokstav i hvert ord om til en stor bokstav, som tilsvarer
    # keyene jeg skrev i ordboken. 
    bruker = str((input("Hvilken bruker vil du vite matplanen til? ")))
    bruker = bruker.title()
    if bruker in matplan.keys():
    # bruker format. funksjonen slik at hvis verdiene i ordboken endres, så vil ikke dette påvirke hva som printes ut
    # i terminalen, som da alltid vil være bruker, matplan[bruker][0] osv. 
        print("{} skal ha {} til frokost, {} til lunsj og {} til middag".format(bruker, matplan[bruker][0], matplan[bruker][1], matplan[bruker][2])) 
    else:
        print("Denne brukeren bor ikke på dette sykehjemmet")

matplanen()

'''
3a) For alle brukernavn, så ville jeg mest sannsyligvis valgt en mengde. Grunnen for dette er fordi man
vil helst at alle brukere på IN1000 har sitt eget unike brukernavn, og en mengde vil derfor ikke tillate 
duplikater. En liste tillatter dette. En ordbok vil også være litt unnødvendig, ettersom jeg antar at det 
bare skal lagre brukernavn, ikke navnet til personen brukernavnet tilhører. Evt hvis man vil lagre navnet til
 en student med brukernavnet, som for eksempel {"Olav Brokke":"s147556"}, så hadde en ordbok vært det beste valget.  
3b) For dette eksempelet, så hadde det nok vært best å bruke en ordbok, ettersom man kan da bruke brukernavet som 
en key, og poengsummen som verdi. En liste og en mengde lagrer ikke verdier i slike koblinger og vil derfor ikke 
være like ideele til dette.  
c) For lotto vinnere så hadde en liste mest sannsynlivis vært best. Det er mulig at en person kan vinne lotto flere 
ganger (veldig lite sannsynelig da) eller to personer kan ha flere navn, så derfor vil man ha muligheten til å 
samme verdi. Ettersom det bare skal lagre navn på vinnere, så er en ordbok unnødvendig for samme grunn som i a). Hvis
man vil lagre tidpunkt for lottovinnere sammen med navn eller vinnersum, så hadde ordbok vært et bedre valg
d) For data på mat som folk er allergiske mot, så er nok en mengde best. Dette er fordi hvis to eller flere personer
er allergiske mot samme mat er det ikke noen vits å skrive dette flere ganger. Hvis man skal planlegge mat til et 
selskap, vil man helst at alle har mulighet til å spise all maten, så da vil man unngå all mat på denne listen. 
'''