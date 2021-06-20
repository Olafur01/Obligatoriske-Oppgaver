def billett_pris():
    # For at jeg skal kunne sammenligne to tall så må jeg konvertere alder til en int. 
    alder = int(input("Hvor gammel er du? "))
    billettpris = 0
    
    # Bruker .format() funksjonen når jeg skriver ut til terminalen, ettersom da kan jeg bare 
    # sette denne lik variabelen og dette skrives derfor ut 
    if alder <= 17:
        billettpris = 30
        print("Prisen for din billett er {} kr.".format(billettpris))
    elif alder > 17:
        billettpris = 50
        print("Prisen for din billett er {} kr.".format(billettpris))
    elif alder >= 63:
        billettpris = 35
        print("Prisen for din billett er {} kr.".format(billettpris))

# Kaller prosedure bare en gang, så kjører jeg bare programmet tre individuelle ganger for hver alder. 
billett_pris()
'''
Hvis man skriver koden slik det står beskrevet i oppgaven så vil man støtte på problemet at pensjonistbiletten
vil aldri bli brukt. Dette er fordi det er innenfor en elif sjekk etter at man sjekker om alderen til personen 
er over 17. Dette betyr at denne if-else sjekken vil stoppe med "elif alder > 17" hver gang, før den går ned til 
neste elif statement. For å fikse dette, så kan man bytte plass på den andre og tredje elif utsagnene eller man 
kan skrive koden slik:
elif alder >= 63:
    bilettpris = 35
    print("Prisen for din bilett er {} kr.".format(bilettpris))
else:
    bilettpris = 50
    print("Prisen for din bilett er {} kr.".format(bilettpris)) 
'''