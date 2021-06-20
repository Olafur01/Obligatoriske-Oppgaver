# Oppgave 1: Utskrift og innlesning av variabler
# Oppg 1.2
# For å få skrevet ut til terminal brukers print funksjonen
print("Hei Student!")

# Oppg 1.3
# For å få innput fra bruker så brukes input() funksjonen. Bruker str funskjonen for å endre input fra bruker om til en string
navn = str(input("Hva er navnet ditt? "))
print("Hei " + "{}".format(navn))

# Oppg 1.4
# Bruker igjen print funksjonen for å få vise tallene i terminalen
tall_1 = 3
tall_2 = 9
print(tall_1)
print(tall_2)

# Oppg 1.5
# For å beregne differansen av tallene, så bruekr jeg abs() funksjonen, slik at det ikke blir et negativt tall
# Print funksjonen er igjen brukt for å skrive ut verdien. Gjøre differanse om til en string, for at den kan kombineres senere.
differanse = abs(tall_1 - tall_2)
print("Differanse: " + str(differanse))


# Oppgave 1.6
# Bruker str funskjonen for å endre input fra bruker om til en string. Dette er fordi begge navnene skal være i string format slik at de kan kombineres
navn_2 = str(input("Gi meg et navn til: "))
sammen = navn + navn_2
print(sammen)

# Oppgave 1.7
# Inkluderer mellomrom i " og " slik at når det blir printet til terminalen blir det et mellomrom mellom navnene og "og"
sammen = navn + " og " + navn_2
print(sammen)
