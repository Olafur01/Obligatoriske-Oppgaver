# Oppgave 2.1 og 2.2 
# Starter med å lage sette tall variabelen til 100, ettersom det er bare når den er lik 0 at løkken skal
# avslutte. Liste og tall variabelene blir også laget før løkken, slik at de er generelle variabler. 
tall = 100
liste = []
while tall != 0:
    # Konverterer all brukerinput om til heltall, slik at det skal sammenlignes med "0" i neste linje. 
    # Ellers hadde en TypeError oppstått.
    tall = int(input("Venligst skriv in et tall: ")) 
    if tall == 0:
        break
    else:    
        liste.append(tall)

# Oppgave 2.3
# Bruker en for løkken for å bare gå raskt gjennom listen 
for i in liste:
    print(i)

# Oppgave 2.4 
# Setter variabelen minSum til 0, og bruker deretter en for løkken for å gå gjennom hele listen og legger
# til hver verdi i minSum variabelen. printer deretter minSum, ved bruk av .format funksjonen. 
minSum = 0
for i in liste:
    minSum += i 
print("Summen av tallene er {}".format(minSum))

# Oppgave 2.5 
# Variabelene for miste og største satt jeg som veldig høye tall til å begynne med, slik at brukeren mest 
# sannsynligvis ikke har skrevet disse inn tidligere. Etter dette så bruker jeg bare en for løkke på listen
# der jeg går gjennom hele listen og prøver å finne den verdien som er minst/størst. Dette gjør jeg ved å 
# gå gjennom hvert tall og sammenligner det med variabelen som er minst/størst. Hvis den er mindre/større så
# erstatter jeg dette tallet med variabelen smallest/largest.   
smallest = 10**10
for i in liste:
    if i < smallest:
        smallest = i 
    else:
        continue 

largest = -10**10
for i in liste:
    if i > largest:
        largest = i
    else:
        continue 

# Konverterer variabelen om til stringer, slik at de kan kombineres med .format funksjonen. 
print("Det største taller er {} og det minste tallet er {}".format(str(largest), str(smallest)))





