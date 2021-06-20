'''
I denne oppgave skal du lage en quiz, hvor det er mulig aa ha flere en et riktig svar. Dette betyr at du 
skal bruke lister for aa sjekke hvor mange riktig svar brukeren klarer aa faa. Dette kan for eksempel
v're hvor mange land som begynner paa bokstaven P eller hvilke lag som har vunnet Tippeligaen. Lag minst
to sp;rsmaal, hvor brukeren faar vite hvor mange riktig svar det fikk til slutt. 
'''

# Løsning 
def quiz():
    svar_1 = input("Hvilke land starter på J? (Skriv et mellomrom mellom hvert svar)").split(" ")
    riktig_svar = ["Japan", "Jamaica", "Jordan", "Jemen"]
    riktig_poeng_sum = len(riktig_svar)
    poeng_sum = 0
    for svar in svar_1:
        if svar.title() in riktig_svar:
            poeng_sum += 1
        else:
            continue
    print("Du fikk {} ut av {} riktig".format(poeng_sum, riktig_poeng_sum))

    svar_2 = input("Hvilke lag har vunnet Premier League? (Skriv et komma og mellomrom mellom hvert svar)").split(", ")
    riktig_svar = ["Manchester United", "Arsenal", "Chelsea", "Blackburn", "Liverpool", "Manchester City", "Leicester City"]
    riktig_poeng_sum = len(riktig_svar)
    poeng_sum = 0
    for svar in svar_2:
        if svar.title() in riktig_svar:
            poeng_sum += 1
        else:
            continue
    print("Du fikk {} ut av {} riktig".format(poeng_sum, riktig_poeng_sum))

quiz()
