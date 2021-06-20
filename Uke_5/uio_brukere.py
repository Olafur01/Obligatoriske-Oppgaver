# Oppgave 4.1
# Lager en åpen ord ved å sette variabelen lik en tom curly brackets
uio_brukere = {}

# Oppgave 4.2
# For å lage et brukernavn som inneholder hele fornavnet og første bokstav av etternavnet, så splittes stringen
# opp i to, fornavn og etternavn. Hele stringen blir også konvertert til lower, slik at alle bokstavene i 
# brukernavnet blir lowercase. Tar så å returnerer hele fornavnet og første bokstav i etternavnet. 
def lagBrukernavn(fullt_navn):
    fullt_navn = fullt_navn.lower().split()
    return fullt_navn[0] + fullt_navn[1][0]

print(lagBrukernavn("Kari Nordman"))

# Oppgave 4.3
# Denne funksjonen tar to parameteret, og for å returnere en epost, så må de egentlig bare kombineres og satt
# sammen med en alfakrøll. Er da dette som blir gjort. 
def lagEpost(brukernavn, suffix):
    return brukernavn + '@' + suffix

print(lagEpost('karin', 'student.matnat.uio.no'))

# Oppgave 4.4
# For å gå gjennom både keys og verdier i en ordbok så bruker items() funksjone. Da kan man refere til keys ved
# bruk av [0] og verdier ved bruk av [1]. Dette vil da kompineres sammen og printes. 
uio_brukere = {'olan':'ifi.uio.no', 'karian':'student.matnat.uio.no'}
def printEposter(uio_brukere):
    for navn in uio_brukere.items():
        print(lagEpost(navn[0], navn[1]))

printEposter(uio_brukere)

# Oppgave 4.5
# For at brukeren skal gå inn i loopen til de skriver inn "s" så settes brukerinput variablene lik en tom string.
# Denne loopen vil da bare avsluttes hvis brukerinput er lik "s". While loopen vil derfor la brukeren legge til 
# så mange bruker input som de vil ha inn i ordboken uio_brukere som ble laget i oppg 4.1. Bruker derfor if-elif-else
# statements for å få riktig output til brukeren. De forskjellige funksjonene laget tidligere i oppgaven bruker
# også om igjen i oppgaven for å gjennomføre riktig løsning. 
brukerinput = ''
while brukerinput != 's':
    brukerinput = input("Skriv in 'i' for å legge ti navn og suffix, skriv 'p' for å printer epostene, eller skriv 's' for å avslutte programmet ").lower()
    if brukerinput == 'i':
        navn = input("Skriv inn fullt navn til en student eller ansatt ved UiO: ")
        suffix = input("Skriv inn epost suffixen som skal brukes")
        uio_brukernavn = lagBrukernavn(navn)
        uio_brukere.update({uio_brukernavn:suffix}) # bruker update funksjonen for å legge til nye keys og verdier
    elif brukerinput == 'p':
        printEposter(uio_brukere)
    elif brukerinput == 's':
        print("Programmet avsluttes")
    else:
        print("Ugyldig Input")

