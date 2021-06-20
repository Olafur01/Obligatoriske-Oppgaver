''' 
Oppgave 1.1 
For å lage en liste så må man bruke brackets for å vise at dette skal være en liste. Når man skal skrive
ut elementer fra listen så må man huske at det første elementet alltid starter på 0, og så går det oppover derfra
'''
liste_1 = [13, 271, 33]
print(liste_1[0], liste_1[2])

""" 
Oppgave 1.2 
En tom liste lages ved å skrive to brackets med ingenting inni 
"""
liste_2 = []
# Bruker split funksjonen for å legge sammen navnene som blir inputtet av bruker, som da blir tildelt til hver 
# variabel. Bruker så .extent() funksjonen for å legge til flere variabler i liste_2. Konverterer også alle 
# strings til lower() slik at i neste deloppgave så blir det lettere å sjekke om de har skrevet navnet mitt i 
# listen. 
navn_1, navn_2, navn_3, navn_4 = input(
    "Please enter four names, seperated by a space ").split(" ")
liste_2.extend((navn_1.lower(), navn_2.lower(), navn_3.lower(), navn_4.lower()))
print(liste_2)

'''
Oppgave 1.3
'''
if "olav" in liste_2:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

'''
Oppgave 1.4
'''
#finner først summen av tallene ved bruk av en for loop, som da tar alle verdiene og 
#legger dem sammen i en ny variabel. Denne er først gitt verdien 0 for at utregningen
#blir riktig. 
summen_av_tallene = 0
for tall in liste_1:
    summen_av_tallene += tall
# Gjør det samme for å finne produktet, men isteden for at variabelen som skal inneholde
# produktet av tallene starter med en verdi av null, starter den isteden med 1 ettersom
# hvis man multipliserer et tall med 0 saa blir det ogsaa 0. 
produktet_av_tallene = 1 
for tall in liste_1:
    produktet_av_tallene *= tall 

liste_3 = [summen_av_tallene, produktet_av_tallene]
print(liste_3)
liste_4 = liste_1 + liste_3
print(liste_4)
# Bruker .pop() funksjonen for å ta vekk den siste verdien i listen. Ved å gjøre det to ganger på rad
# så blir man kvitt de to siste elementene av listen
liste_4.pop()
liste_4.pop()
print(liste_4)





