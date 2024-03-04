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
            arsmedel(pisadata)
            nordtabell_print(pisadata)
  
            
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
            value =int(row[columnindex]) #använder mig av row[col index för att bestäma villken column vi letar i]
            totalsum += value #använder mig av += för att sum datan vi får för varje column 
            values += 1 #lägger till i values om det genomförs och beräknar sedan antal som finns i listan
        except ValueError:# om det går inte att ändra så hoppar den över.
            pass
    return round(totalsum/values) #beräknar medelvärdet


def arsmedel(list2):
    armedel= []
    for columnindex2 in range (13, len(list2[0])):
        medelvärdet= kolumnmedel(list2, columnindex2) # använder oss av funktionen kolumnmedel för att beräkna medelvärdet 
        armedel.append(medelvärdet) # och sedan lägga till den i listan 
    return armedel

def nordtabell(list3,lista4):

    land = ["Sweden","Norway","Denmark","Finland","Iceland"] #skapar en lista för att söka på länder
    länder = [] #en lista 

    for w in land: # skapar for loops för att söka på de länder vi letar efter
        for rad in list3:
            if rad[0] == w: #söker på rad 0 och sedan lägger till den i listan om det matchar listan
                länder.append([rad[0],rad[13:len(rad)]])
    år = [2018,2015,2012,2009,2006,2003] 
    print("\nKunskapsutveckling i matematik enligt PISA-undersökningen 2003 – 2018.") #skriver ut Nordtabell
    print("                               Länder:")
    print("--------------------------------------------------------------------------------------")
    print("År  Sweden Norway Denmark Finland Iceland          Medelvärde alla länder")
    print("--------------------------------------------------------------------------------------")
    for i in range(len(år)):
        print (år[i], länder[0][i], länder[1][i],länder[2][i],länder[3][i],länder[4][i],länder[5][i],länder[6][i],)


def nordtabell_print(list4):
    arsmedel2 = arsmedel(list4) #lägger in medelvärdet
    medelvärdet = [] #skapar ny lista för att inte få probelm mede andra uppgiften
    for jjj in arsmedel2: # for loops för att lägga in ny lista
        medelvärdet.append(jjj) # lägger i lista
        
    flipdata2 = nordtabell(list4) 
    newlist = []
    for jj in flipdata2:
        newlist.append(jj) #samma
    
    #skapar år lista för att skriva ut



    for år,flipdata2,arsmedel2 in zip(år,flipdata2,arsmedel2): # använder mig av zip för struktur
        print(f"{år} {flipdata2}                 {arsmedel2} ") # och skriver ut värden år nord länderna och medelvärden
    
        pass
    nyår = [2018,2015,2012,2009,2006,2003]  # skapar ny år lista för att inte påverka denna uppgift   
    länder_int = [[int(x) for x in sublist] for sublist in newlist] # gör nord länderna till ints för att sedan lägga in det i nordgraf
    länder_int = [list(row) for row in zip(*länder_int)] # använder mig av av for loops för att vänd listan igen för att matcha grafen
    

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
    plt.plot(nyår, medelvärdet,label="medel")
    plt.xlabel("År")#x namn
    plt.ylabel("Poäng")# y namn
    plt.title("PISA-undersökningen 2003 – 2018") #Titel
    plt.grid(True)#grids.
    plt.legend()#lägger till en ruta i grafen som visar vilken linje som till hör vilket land
    plt.show()#visa graf

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
