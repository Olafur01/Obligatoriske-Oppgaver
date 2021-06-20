'''
1. For å kommunisere med brukeren så bruker vi input funksjonen. Det stilles også spørsmål
som gjør det enkelt for bruker å vite hva de skal skrive. For å få skrevet dette ut til
terminalen, så brukes print funksjonen, og format funksjonen for strings. .format funksjonen
gjør det enkelere å endre på det som skal skrives ut senere, hvis man vil gjøre dette
'''
navn = input("Skriv inn navn: ")
sted = input("Hvor kommer du fra? ")
print("Hei, {}! Du er fra {}.".format(navn, sted))

"""
2. For å gjennomføre denne oppgaven så laget jeg en funksjon med two parametere. Disse blir
det samme som vi fikk som input fra brukeren i del 1, navn og sted. Når man da kaller denne
funksjonen, så bruker skriver man inn her hva som skal være navnet til personen, og så hvilket
sted de kommer fra. Med funksjoner så brukes "return", fordi da avsluttes funksjonen og man vil
returnere denne verdien. Her er samme kode som i deloppgave 1 brukt, med .format. For å få
skrevet ut det som returneres av funksjonen til terminalen, så brukes print funksjonen.
"""
def utskriftsfunksjon(navn, sted):
    return "Hei, {navn}! Du er fra {sted}.".format(navn=navn, sted=sted)


print(utskriftsfunksjon("Donald Duck", "Andeby"))
print(utskriftsfunksjon("Espen Askeladen", "Oslo"))
print(utskriftsfunksjon("Minni Mus", "Museby"))
