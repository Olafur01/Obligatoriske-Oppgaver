'''For denne oppgaven så bruker jeg igjen input() funksjonen for å få svar fra brukeren.
Dette vil jeg lagre som variablen "svar". Fra dette så bruker jeg en if-sjekk. Gjør også
inputen om til en string ved str() funksjonen, slik at det bli lettere å sammenligne senere
i programmet'''
svar = str(input("Vil du ha en brus? "))

# Bruker if, elif og else statements, slik at programmet går gjennom hver beslutning som en helhet.
# Legger også til en bool statement for "Ja", "ja" "JA", slik at unansett hvordan bruker skriver dette så blir det tolket på samme på.
# Dette samme blir gjort for "Nei"

if svar == "JA" or svar == "Ja" or svar == "ja":
    print("Her er en brus")
elif svar == "NEI" or svar == "NEi" or svar == "Nei" or svar == "nei":
    print("Den er grei")
else:
    print("Det forsto jeg ikke helt")
