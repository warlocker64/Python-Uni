# Skriv en inledande kommentar som talar om vad programmet gör.
#....
# Placera dina modulimpoter här:
import matplotlib.pyplot as plt
import csv

def nordland(list3):

    land = ["Sweden","Norway","Denmark","Finland","Iceland"] 
    länder = [] 
    for w in land: # skapar for loops för att söka på de länder vi letar efter
        for rad in list3:
            if rad[0] == w: 
                länder.append(rad)
    return länder
# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:
def read_file(filnamn):
    pisadata=[]
    with open (filnamn, "r") as file: #Öppnar filen och sedan läser
        read = csv.reader(file, delimiter = ";")
        for rad in read: #läser filen och använder for sats för att lägga in i en lista
            pisadata.append(rad)
    return pisadata


# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:
    
def år2018(lista,kol): 
    l18=[]
    for rad in lista[2:]:
        l18.append([rad[0], rad[kol]])
    sortedlist=sorted(l18,key=lambda x:x[-1])
    best = sorted(sortedlist[-10:], key=lambda x:x[-1], reverse=True)
    worst = sortedlist[:10]
    print("De tio länder som hade bäst resultat år 2018")
    print("-"*45)
    print("Land                             Resultat")
    print("-"*45)
    for rad in best:
        print(f'{rad[0]:<15}{rad[1]:>23}')
    print("-"*45)
    print("De tio länder som hade sämst resultat år 2018")
    print("-"*45)
    print("Land                             Resultat")
    print("-"*45)
    for rad in worst:
        print(f'{rad[0]:<15}{rad[1]:>23}')
    print("-"*45)


# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
# Skriv din kod här:
def kolumnmedel(list, columnindex):
    totalsum = 0
    values = 0
    
    for row in list[2:]:
        try:
            value =int(row[columnindex]) 
            totalsum += value 
            values += 1 
        except ValueError:# om det går inte att ändra så hoppar den över.
            pass
    return round(totalsum/values) #beräknar medelvärdet


def arsmedel(list2):#Funktion för medelvärdet mellan 2003 till 2019
    armedel= []
    flipdata1 = [list(row) for row in zip(*list2)]
    j = -1
    for i in flipdata1:
        j+= 1
        if i[1] == "medel":
            medelvärdet= kolumnmedel(list2, j) # använder oss av funktionen kolumnmedel för att beräkna medelvärdet 
            armedel.append(medelvärdet)
    return armedel


def årtal(år):#Skapar årtal för använding 
    nyår= []
    årlist = []
    for jj in år:
        firstlist = jj[-6:]
        årlist.append(firstlist)

    flipdata2 = [list(row) for row in zip(*årlist)] #behöver vända så det underlättar kod
    for år in flipdata2:
        
        nyår.append(år[0])
    nyår = [int(i) for i in nyår]
    return nyår
    
def nordtabell(list4,medel,länder):#Skapar Nordtabell 
    arsmedel2 = medel
    flipdata = länder
    data = [] 
    for i in flipdata:
        del i[:-6]
        data.append(i)
    flipdata2 = [list(row) for row in zip(*data)] #Har den för att matcha kod

    
    år = årtal(list4)
    

    print("\nKunskapsutveckling i matematik enligt PISA-undersökningen 2003 – 2018.") 
    print("                               Länder:")
    print("--------------------------------------------------------------------------------------")
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format("År", "Sweden", "Norway", "Denmark", "Finland", "Iceland", "Medelvärde alla länder"))
    
    print("--------------------------------------------------------------------------------------")
    for år,flipdata2,arsmedel2 in zip(år,flipdata2,arsmedel2): # använder mig av zip för struktur
        print(f"{år:<10}{flipdata2[0]:^10}{flipdata2[1]:^10}{flipdata2[2]:^10}{flipdata2[3]:^10}{flipdata2[4]:^10}{arsmedel2:^10} ")
    
    
def nordtabellgraf(list5,medel,länder): #skapar Nordgraf 
    arsmedel2 = medel
    nländer = länder
    år = årtal(list5)
    länder_int = [[int(x) for x in sublist] for sublist in länder] #ändrar vä'rden till int för att användas i graf
    
    sweden = länder_int[0] #väljer ut länderna från norden
    norway = länder_int[1]
    denmark = länder_int[2]
    finland = länder_int[3]
    iceland = länder_int[4]
    plt.plot(år, sweden,label="Swden") # skriver ut år och även land och label
    plt.plot(år, norway,label="Norway")
    plt.plot(år, denmark,label="Denmark")
    plt.plot(år, finland,label="Finland")
    plt.plot(år, iceland,label="Iceland")
    plt.plot(år, medel,label="medel")
    plt.xlabel("År")
    plt.ylabel("Poäng")
    plt.title("PISA-undersökningen 2003 – 2018") 
    plt.grid(True)
    plt.legend()
    plt.show()



# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:

def battresamre(pisadata, bättre):#Detta definierar en funktion som tar två parametrar pisadata som är en lista och bättre som en boolean variabel som letar efter förbättringar och försämringar
    if bättre:# kontrollerar  om värdet på bättre är sant eller falskt.
        print('Länder som hela tiden har förbättrat sina resultat mellan 2003-2018')
    else:
        print('Länder som hela tiden har försämrat sina resultat mellan 2003-2018')
    
    print('--------------------------------------------------------------------------------')
    print('{:<20} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format("Land", "2018", "2015", "2012", "2009", "2006", "2003"))
    print('--------------------------------------------------------------------------------')

    for rad in pisadata[2:]: #en loop som går igenom varje rad i pisadata index 2 för att hoppa över de två första raderna som inte ger data
        land = rad[0] # tar landets namn från första indexet i varje rad
        resultat = rad[13:19]  # tar resultat från varje år mellan 2018 till 2003
        resultat = [int(r) if r else None for r in resultat] #gör de resultat från ovan till heltal
       
       #Denna två kontrollerar om det blir förbättring för varje land
        if bättre: 
            if all(resultat[i] >= resultat[i + 1] for i in range(len(resultat) - 1) if resultat[i] is not None and resultat[i + 1] is not None):
                print('{:<20} '.format(land) + ' '.join('{:<10}'.format(res) if res is not None else ' ' * 10 for res in resultat))

        #Denna kontrollerar om det blir försämring för varje land
        else: 
            
            if all(resultat[i] <= resultat[i + 1] for i in range(len(resultat) - 1) if resultat[i] is not None and resultat[i + 1] is not None):
                print('{:<20} '.format(land) + ' '.join('{:<10}'.format(res) if res is not None else ' ' * 10 for res in resultat))




# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:


def kvinna_man(data):
    print('År och länder när kvinnorna presterar bättre än männen under åren 2003–2018.')   # skriver ut en rubrik
    print('-' * 76)                                                                         # skriver ut 76st -
    print(f'{"År":<10}{"Land":<22}{"Kvinnor":<15}    {"Män"}')                              # skriver ut tabellhuvudet 
    print('-' * 76)                                                                         # skriver ut 76st -
    
    for år in range(2018,2002 , -3):                                                         # yttre loop för åren mellan  2003 och 2018 med 3 år mellanrum
        rad_1 = True                                                                        # flagga för att hålla reda på om det är den första matchade raden för det aktuella året.
        for rad in data[2:]:                                                                # inre loop för att genomgå över raderna i data  från index 2 
            diff = (2018 - år) / 3                                                          # beräknar skilladen mellan 2018 och det aktuella året och delar skilladen med 3         
            man, kvinna = 1 + diff * 2, 2 + diff * 2                                        # beräknar indexen för män och kvinnor        
            man, kvinna = int(man), int(kvinna)                                             # gör om indexen till heltal
            kvinnaP, manP = int(rad[kvinna]), int(rad[man])                                 # hämtar procenttal för kvinnor och män  i den nuvarande rad i data 
            

            if kvinnaP > manP:                                                              # kollar om kvionnor pestrerar bättre än män 
                if rad_1:                                                                   # kontrollerar om det är den första matchade raden för det aktuella året 
                    print(f'{år:<10}', end='')                                              # printar ut året
                    rad_1=False 
                else:                                                                       # om rad_1 är falsk  skrivs en tom sträng    
                    print(' ' * 10, end='')                                                 #''
                print(f'{rad[0]:<22}  {kvinnaP:<17}{manP}')                                 # printar landets namn och värdet för män och kvinnors presterande
        if not rad_1:
            print()


                    

# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl.uppgiftsbeskrivningen.
# Skriv din kod här:
while True:
    print("1. Läs in csv-filen")
    print("2. Bästa resp. sämsta resultat år 2018")
    print("3. Matematikkunskaper i norden år 2003 – 2018.")
    print("4. Kontinuerligt förbättrat resp. försämrat år 2003 – 2018.")
    print("5. Kvinnor presterar bättre än män under åren 2003–2018")
    print("6. Avsluta programmet.")
    print("Välj ett menyalternativ (1-6):")
    val = int(input()) #frågar efter num och använder if satser "Meny" för att göra beslut
    if val == 1:
            filnamn =input("Ange filnamn eller tryck bara Enter för att använda data.csv: ") or 'pisadata.csv'

            pisadata= read_file(filnamn)
            print(pisadata[:5])
            
    elif val ==2:
        år2018(pisadata, 13)
        
    elif val ==3:
        arsmedel(pisadata)
        nordländer = nordland(pisadata)
        medelvAr = (arsmedel(pisadata))
        nordtabell(pisadata,medelvAr,nordländer)
        nordtabellgraf(pisadata,medelvAr,nordländer)
        pisadata= read_file(filnamn)
        
  
          
    elif val ==4:
        battresamre(pisadata, True)  # För länder som har förbättrat sina resultat
        battresamre(pisadata, False) # För länder som har försämrat sina resultat

            
    elif val ==5:
        kvinna_man(pisadata)
                   
    elif val ==6:
        break