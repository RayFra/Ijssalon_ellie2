def mijn_functie_1(nummer):
    resultaat = nummer * nummer 
    return resultaat 

input_nummer = int(input("Voer een nummer in: "))

uitkomst = mijn_functie_1(input_nummer)
print(uitkomst)


def mijn_functie_2(a, b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst
  
waarden = [(12,3), (12,2), (10,5), (100,20)]

for a, b in waarden:
    resultaat = mijn_functie_2(a, b)
    print(f"Voor a={a} en b={b}: {resultaat}")
 
    
    
    