print("-------------------------------------------------")
pengar = int(input("Hur mycket pengar har du ? "))
while pengar < 0:
    print("Negativ summa kann ej anges")
    pengar = int(input("Försök igen. Hur mycket pengar har du ? "))

år = int(input("När är du född? "))
print("-----------------------------------------------------")
ålder = 2024-år
while år > 2024 or år < 1874:
    print("felaktig år tal")
    år = int(input("Försök igen ålder måste vara mellan 0-150 år, hur gammal är du?  "))
    
else:
    print(f"Hur mycket pengar du har {pengar} kr")
    print(f"När du född {år}")
    print(f"Du är såldes {ålder} år gammal")
    print("Kontroll sker...")

    if ålder >= 18:
        print("Billjetten kostar 100:- för 18år+")
        if pengar > 100:
            print("Du har råd")
        elif pengar < 100:
            print("Du har inte råd ")
    elif ålder < 18 and ålder >= 7:
        print("Billjetten kostar 50:- för 7år+")
        if pengar > 50:
            print("Du har råd")
        elif pengar < 50:
            print("Du har inte råd ")
    elif ålder <7:
        print("Det är grattis att åka för barn under 7 år")
        if pengar > 0:
            print("Du har råd")
        

    

