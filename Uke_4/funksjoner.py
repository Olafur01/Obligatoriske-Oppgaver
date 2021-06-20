# Oppgave 1.1
# Denne oppgave inkluderer to parametere som brukes i funksjonen. De gjøres om til string
# slik at de kan legges sammen med tekststrengen som returneres fra verdien 
def adder(tall1, tall2):
    return "Summen av tallene er " + str(tall1 + tall2) 

print(adder(14, 15))
print(adder(255, 57))

# Oppgave 1.2
# Har skrevet oppgaven i en multiline string ettersom det bare var oppg. 1.3 som skulle kjøres
# men den bruker lignde ideerer som i neste oppgave. Gjør alle ordene i tekstrengen om lowercase
# når man kjører en for løkke for å sjekke om en bokstav er i tekstrengen, så vil en "B" bli det 
# samme som en "b". Lager også en variabe kalt "counter", som brukes for å telle hvor mange ganger
# en bokstav intreffer i tekststrengen. 

'''tekststreng = input("Skriv inn en tekststreng: ").lower()
bokstav = input("Velg en bokstav ")
counter = 0
for letter in tekststreng:
    if letter == bokstav:
        counter += 1
    else:
        continue 
print(counter)
'''

# Oppgave 1.3 
# Lager først variablene minTekst og minBokstav utenfor funksjonen, slik at de er generelle variabler,
# ikke lokale. I funksjonen blir bare disse to variabelene brukt på sammen måte som i 1.2, bare at man
# returnerer counter variabelen, isteden for å printe den. 
minTekst = input("Skriv inn en tekststreng: ").lower()
minBokstav = input("Velg en bokstav ")


def tellForekomst(minTekst, minBokstav):
    counter = 0
    for letter in minTekst:
        if letter == minBokstav:
            counter += 1
        else:
            # Velger å bruke denne commandoen, slik at hvis det ikke er samme bokstav så forsetter 
            # løkken bare videre til neste bokstav
            continue 
    return counter

print(tellForekomst(minTekst, minBokstav))
