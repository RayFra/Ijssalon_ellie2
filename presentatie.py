def presenteer(mijn_dict, totaal):
    for item, prijs in mijn_dict.items():
        print(f"{item} : {prijs} euro")

    print("==================")
    print(f"totaal : {totaal} euro")

mijn_dict = {"vis" : 10, "vlees" : 25, "overig" : 15}
totaal = sum(mijn_dict.values())

presenteer(mijn_dict, totaal)

