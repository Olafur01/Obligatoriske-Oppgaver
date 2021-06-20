'''
Oppgavetekst
I denne oppgaven skal man lage en quiz, hvor man får input fra brukeren. Denne quizen skal inneholde 3 spørsmål,
hvor hvert riktig svar gir brukeren en positiv respons, mens et feil svar gir et negativt et. Man skal bruke beslutninger
(if/else) for å løse dette. Det er viktig å huske at brukeren kan skrive svarene sine med bare store bokstaver eller små,
så dette må tas i betraktning. En måte å løse dette på er å bruke lower. funksjonen.
'''


# LØSNING
spørsmål_1 = str(input("Hva er hovedstaten i Norge? ").lower())
if spørsmål_1 == "oslo":
    print("Riktig Svar")
else:
    print("Feil Svar")

spørsmål_2 = str(input("Hvilket år startet andre verdenskrig? ").lower())
if spørsmål_2 == "1939":
    print("Riktig Svar")
else:
    print("Feil Svar")

spørsmål_3 = str(input("Hvilket lag spiller Lionel Messi for? ").lower())
if spørsmål_3 == "barcelona":
    print("Riktig Svar")
else:
    print("Feil Svar")
