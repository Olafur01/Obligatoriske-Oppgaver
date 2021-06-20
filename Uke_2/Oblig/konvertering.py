"""
For dette programet så blir variabelene mine kalt det som passer de best med tanke
på hvilken informasjon de inneholder, derfor blir det temp_fahrenheit for temperatur
i fahrenheit. Det er det samme for celcius variabelen. Input verdien fra brukeren
konverteres til en heltall, slik at vi ikke støtter på noeTypeError, hvor det er mulig
at man prøver å kombinere en string og et tall underkonverteringen. Ettersom jeg blir
instruertat celcius skal tilsvare 37,78 grader nårfahrenheit verdien er 100, så gjøres
bruker jeg "round" funksjonen, og passer på atprogrammet runder til de to første desimal
tallene.
"""
temp_fahrenheit = int(input("Hva er temperaturen ute gitt i fahrenheit?"))
print(temp_fahrenheit)
# Når jeg bruker round funksjonen, så er den slik at man først skriver verdien som skal printes
# og så skriver man et komma og så hvor mange desimal tall som skal inkluderes.
temp_celcius = round((temp_fahrenheit - 32) * 5 / 9, 2)
print(temp_celcius)
