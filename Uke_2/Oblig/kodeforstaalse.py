'''
1. Koden er ikke lovelig hvis input variabelen fra brukeren er under 10, fordi da vil print()
funksjonen i betingelses utsagnet bli kjørt. Denne er ikke lovelig ettersom man prøver å slå sammen
en string og et heltall. Hvis inputten fra brukeren er 10 eller over så vil ikke denne betingelsen
bli kjørt, og derfor vil ikke den feilen oppstå.
2. Problemet man vil støtte på i denne koden er at man prøver å kombinere heltall inputtet fra brukeren
med en string verdi, hvis heltall verdien er under 10. I python så er ikke dette mulig og vil føre til en
TypeError, ettersom man prøver å slå sammen en string og heltall. Man kan løse dette problemet ved å
konvertere "b" til en sting ved å bruke str() funksjonen. Dette betyr at koden på siste linje vil se
slik ut: print(str(b) + "Hei!")
 '''
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")
