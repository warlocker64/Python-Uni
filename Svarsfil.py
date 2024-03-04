# Skriv en inledande kommentar som talar om vad programmet gör.
#....
# Placera dina modulimpoter här:
import matplotlib.pyplot as plt
import csv
def read_file(filnamn):
    pisadata=[]
    with open (filnamn, "r") as file: #Öppnar filen och sedan läser
        read = csv.reader(file, delimiter = ";")
        for rad in read: #läser filen och använder for sats för att lägga in i en lista
            pisadata.append(rad)
    return pisadata

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
def menytxt(): #Meny 
    print("1. Läs in csv-filen")
    print("2. Bästa resp. sämsta resultat år 2018")
    print("3. Matematikkunskaper i norden år 2003 – 2018.")
    print("4. Kontinuerligt förbättrat resp. försämrat år 2003 – 2018.")
    print("5. Kvinnor presterar bättre än män under åren 2003–2018")
    print("6. Avsluta programmet.")
    print("Välj ett menyalternativ (1-6):")

def meny(): # Använder whileloop för att skapa en meny. 
    while True:
        menytxt()
        val = int(input()) #frågar efter num och använder if satser "Meny" för att göra beslut
        if val == 1:
            filnamn =input("Ange filnamn eller tryck bara Enter för att använda data.csv: ") or 'pisadata.csv'

            pisadata= read_file(filnamn)
            print(pisadata[:5])
            
        elif val ==2:
            år2018(pisadata, 13)
            
        elif val ==3:
            nordländer = nordland(pisadata)
            medelvAr = (arsmedel(pisadata))
            nordtabell(medelvAr,nordländer)
            nordtabellgraf(medelvAr,nordländer)
            pisadata= read_file(filnamn)
  
        elif val ==4:
            battresamre(pisadata, True)  # För länder som har förbättrat sina resultat
            battresamre(pisadata, False) # För länder som har försämrat sina resultat

            
        elif val ==5:
            print(2)
                   
        elif val ==6:
            break


# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:
    
def år2018(lista,kol): # Använder mig av val så det inte behvös repeteras
    l18=[]
    for rad in lista[2:]:
        l18.append([rad[0], rad[kol]])
    sortedlist=sorted(l18,key=lambda x:x[-1])
    best = sorted(sortedlist[-10:], key=lambda x:x[-1], reverse=True)
    worst = sortedlist[:10]
    print("De tio länder som hade bäst resultat år 2018")
    print("----------------")
    print("Land   Resultat")
    print("----------------")
    for rad in best:
        print(rad[0],rad[1])
    print("----------------")
    print("De tio länder som hade sämst resultat år 2018")
    print("----------------")
    print("Land   Resultat")
    print("----------------")
    for rad in worst:
        print(rad[0],rad[1])
    print("----------------")


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
    for years in range(2003, 2019): # söker mellan 2003 till 2019
        for index,item in enumerate(list2[0]): 
            if str(years) in item or "medel" in item.lower(): 
                columnindex2 = index
                break
        else:
            continue
        medelvärdet= kolumnmedel(list2, columnindex2) # använder oss av funktionen kolumnmedel för att beräkna medelvärdet 
        armedel.append(medelvärdet)
    return armedel

def nordtabell(medel,länder):#Skapar Nordtabell 
    arsmedel2 = medel
    flipdata = länder
    data = [] 
    for i in flipdata:
        del i[:-6]
        data.append(i)
    flipdata2 = [list(row) for row in zip(*data)] #Har den för att matcha kod

    
    år = [2018,2015,2012,2009,2006,2003] 
    

    print("\nKunskapsutveckling i matematik enligt PISA-undersökningen 2003 – 2018.") 
    print("                               Länder:")
    print("--------------------------------------------------------------------------------------")
    print("År  Sweden Norway Denmark Finland Iceland          Medelvärde alla länder")
    print("--------------------------------------------------------------------------------------")
    for år, flipdata2, arsmedel2 in zip(år, flipdata2, arsmedel2): 
        flipdata2_str = ' '.join(number + ' '*3 for number in flipdata2)
        print(f"{år}   {flipdata2_str}                   {arsmedel2}")

def nordtabellgraf(medel,länder): #skapar Nordgraf 
    arsmedel2 = medel
    nländer = länder
    nyår = [2018,2015,2012,2009,2006,2003]
    länder_int = [[int(x) for x in sublist] for sublist in länder] #ändrar vä'rden till int för att användas i graf
    
    sweden = länder_int[0] #väljer ut länderna från norden
    norway = länder_int[1]
    denmark = länder_int[2]
    finland = länder_int[3]
    iceland = länder_int[4]
    plt.plot(nyår, sweden,label="Swden") # skriver ut år och även land och label
    plt.plot(nyår, norway,label="Norway")
    plt.plot(nyår, denmark,label="Denmark")
    plt.plot(nyår, finland,label="Finland")
    plt.plot(nyår, iceland,label="Iceland")
    plt.plot(nyår, medel,label="medel")
    plt.xlabel("År")
    plt.ylabel("Poäng")
    plt.title("PISA-undersökningen 2003 – 2018")
    plt.grid(color = 'black') 
    plt.gca().set_facecolor('lightblue')
    plt.legend()
    plt.show()
    

def kvinna_man(list2):
    listamf = []
    for row in listamf:
        del row[-6:]
        listamf.append(row)
    for j in listamf: # skapar loops för att få värden till ints så det är enklare att jämnföra
        for i in range(1, len(j)):#använder mig av len för hur många loops 
            try:
                j[i] = int(j[i])
            except ValueError:# om det inte går att göra det till en int så fortsätter den
                pass
    newlist= []
    for jj in newlist:
        for ii in range(1, len(jj), 2): #vi använder oss av for loops för att beräkna var 2 column
            kvinna= (jj[ii+1]) #flyttar fram för att få fram kvinna
            män= (jj[ii]) #män
            if kvinna > män:
                newlist.append(kvinna)#X

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
# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl.uppgiftsbeskrivningen.
# Skriv din kod här:
meny()