from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer 


print(aanbieding_1("Aardbei", 4, 0.1)) 

def inkomsten_totaal(inkomsten):
    
    waarden = [220, 430, 125, 160, 205, 90, 345]
    inkomsten = sum(waarden)
    bedrag = inkomsten * 0.09
    print(inkomsten)
    print(f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {bedrag} euro btw betaald dient te worden.")
    return inkomsten

inkomsten_totaal(None)

def laag_hoog(mijn_lijst):
    waarden = [220, 430, 125, 160, 205, 90, 345]
    mijn_lijst = max(waarden), min(waarden)
    print(mijn_lijst)
    return mijn_lijst

laag_hoog(None)

def gemiddelde(mijn_lijst):
    waarden = [220, 430, 125, 160, 205, 90, 345]
    totaal = sum(waarden)
    gemiddelde_inkomsten = totaal / len(waarden)
    print(f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro. ")
    return gemiddelde_inkomsten

gemiddelde(None)

def meervoudig(invoer_lijst):
    nieuwe_waarden = [10, 5, 3, 2, 1, 9]
    nieuwe_lijst = laag_hoog(nieuwe_waarden)
    print(max(nieuwe_waarden), min(nieuwe_waarden))
    return nieuwe_lijst

meervoudig(None)

def combinatie(invoer_lijst_2):
    korte_lijst = invoer_lijst_2
    laag_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer




    







    


