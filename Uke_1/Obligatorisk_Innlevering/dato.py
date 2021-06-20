# For at bruker skal forstå hvordan man skal skrive inn datoen, så legges dette til med input() funksjonen
# Ber også bruker skrive inn to forskjellige inputs for hver dato slik at sammenligningen blir enklere
# Bruker og int() funksjonen for og forsikre at det blir heltall
dag_1 = int(input(
    "Vennligst skriv inn dagen for første dato (Dette skal være et heltall): "))
måned_1 = int(input(
    "Vennligs skriv in måned for første dato, med heltall (Eksempelvis er mars = 3): "))
dag_2 = int(
    input("Vennligst skriv inn dagen for andre dato (Dette skal være et heltall): "))
måned_2 = int(input(
    "Vennligs skriv in måned for første dato, med heltall (Eksempelvis er mars = 3): "))

# For beslutningen så vurderes månedene først, og hvis disse er like så vurderes dagene. Hvis disse er også like
# så skrives det ut at datoene er like.
if måned_1 < måned_2:
    print("Riktig rekkefølge")
elif måned_1 > måned_2:
    print("Feil rekkefølge")

if måned_1 == måned_2:
    if dag_1 < dag_2:
        print("Riktig rekkefølge")
    elif dag_1 > dag_2:
        print("Feil rekkefølge")
    else:
        print("Samme dato!")
