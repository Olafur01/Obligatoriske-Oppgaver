# Oppgave 1.1
# For at funksjonen skal gi et tall og ikke en NoneType verdi, så bruker jeg return og legger verdiene 
# samme på samme linje for at det skal redusere mengde med kode. Denne prosessen videreføres til neste
# oppgave. 
def addisjon(tall1, tall2):
    return tall1 + tall2

print(addisjon(3, 20))

# Oppgave 1.2 
def subtraksjon(tall1, tall2):
    return tall1 - tall2

# Bruker round funksjonen, som tar to argumenter, det ene er tallet en vil runde, og det andre er hvor mange
# desimaler man vil ha. Bestemmer meg for at det å printe tall med to desimaler er best 
def divisjon(tall1, tall2):
    return round(tall1 / tall2, 2)

# Her gjennomføres flere assert utsagn. Maa derfor sette det lik det jeg tror det blir. Hvis dette er feil
# blir en assertion error. 
assert addisjon(5, 5) == 10
assert addisjon(-5, 20) == 15
assert addisjon(-12, -13) == -25
assert subtraksjon(10, 6 ) == 4
assert subtraksjon(-20, -100) == 80
assert subtraksjon(50, -20) == 70
assert divisjon(2, 3) == 0.67
assert divisjon(-2, -3) == 0.67
assert divisjon(-10, 2) == -5

# Oppgave 1.3 
# Bruker assert her slik at hvis noen inputter et tall under 0 tommer, så vil dette føre til en assertion 
# error, og stoppe programmet. 
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

print(tommerTilCm(12))

# Oppgave 1.4 
# Skriver denne funksjonen som først printer ut at det er utregninger som blir gjort og at bruker må
# skrive inn to tall. Disse tallene blir konvertert til heltall, ellers ville en legge error oppstå 
# i subtraksjon og divisjonsfunksjonene. Addisjon funksjonen hadde kjørt, men da legger man isteden sammen
# to strings, og får derfor feil "tall"
def skrivBeregninger():
    print("Utregninger")
    tall1 = int(input("Skriv in tall 1: "))
    tall2 = int(input("Skriv in tall 2: "))

    # Bruker f string funksjone for å forenkle prosessen av printing og få tallene automatisk til å 
    # konvertes til strings. 
    print(f"Summen av disse tallene er {addisjon(tall1, tall2)}")
    print(f"{tall1} minus {tall2} er {subtraksjon(tall1, tall2)} ")
    print(f"{tall1} delt på {tall2} er {divisjon(tall1, tall2)} ")
    
    # Printer først ut at dette er en konvertering, før man spør bruker etter input. Denne inputten 
    # konverters til et heltall for ellers vil en TypeError oppstå. 
    '''print("Konvertering fra tommer til cm:")
    antallTommer = int(input("Skriv in en lengde i tommer: "))
    print(f"Lengden i cm er {tommerTilCm(antallTommer)}")'''

# Kaller på funskjonen for at den skal kjøres
skrivBeregninger()

