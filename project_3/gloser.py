class Kategori():
    def __init__(self, filnavn):
        self._kategorier = {}
        self._filnavn = filnavn
        self._lesfil(self._filnavn)

    def skrivUt(self):
        self._hopp()
        self._sorter()
        for nokkel in self._kategorier:
            print()
            print()
            print()
            print()
            print()
            print(nokkel + ":")
            self._kategorier[nokkel].skrivUt()
            print()

    def sok(self, input):
        self._hopp()
        input = self._gjenkjenn(input)
        print("Fant:", input)
        print()
        if input in self._kategorier:
            print(input + ":")
            self._kategorier[input].skrivUt()
            return
        else:
            for nokkel in self._kategorier:
                if self._kategorier[nokkel].sok(input) == True:
                    print()
                    return
        print()
        print(input, "ikke funnet")
        print()

    def _gjenkjenn(self, input):
        ordbok = {"å":"pøæ", "æ":"åø-", "ø":"lpåæ.-", "/":"6yu8&(","-":".øæ", " ": "xcvbnm,", "§": "1", "q":"12wsa", "w":"q23esa", "e":"w34rds", "r":"e45tfd", "t":"r56ygf", "y":"t67uhg", "u":"y78ijh", "i":"u89okj", "o":"i90plk", "p":"o0+åøl", "å":"p+\¨æø", "a":"qwsz", "s":"awedxz", "d":"serfcx", "f":"drtgvc", "g":"ftyhbv", "h":"gyujnb", "j":"huikmn", "k":"jiol,m", "l":"kopø.,", "ø":"lpåæ-.", "æ":"øå¨-", "z":"asx", "x":"zsdc ", "c":"xdfv ", "v":"cfgb ", "b": "vghn ", "n":"bhjm ", "m":"njk, "}
        sjekket = {}
        liste = []


        fil = open(self._filnavn)
        for linje in fil:
            modInput = list(input.lower())
            likhet = 0
            nabo = 0
            splittet = linje.strip().split(" | ")
            bruk = list(splittet[1].lower())
            liste.append(splittet[1])

            if len(bruk) == len(modInput):
                likhet += 1 #Likhet for lik lengde på ordene
            else:
                while len(bruk) != len(modInput):
                    if len(bruk) > len(modInput):
                        modInput.append("§")
                    if len(bruk) < len(modInput):
                        bruk.append("§")
                assert len(bruk) == len(modInput) #Krever at de er like lange
            for i in range(len(bruk)): #Går igjennom bokstavene i input
                j = i
                if j == 0:
                    j += 1
                elif j == len(bruk)-1:
                    j -= 1

                if bruk[i] == modInput[i]:
                    if bruk[i] != "§":
                        likhet += 1 #Likhet for samme bokstav på samme sted
                elif (bruk[i] == modInput[j]):
                    if bruk[i] != "§":
                        likhet += 0.5 #Likhet for omstokkede bokstaver ABC = BAC gir totalt 1 poeng herfra (0.5 fra B, og 0.5 fra A)
                elif bruk[i] in ordbok[modInput[i]]:
                    likhet += 0.25 #Likhet for bokstav ved siden av på tastaturet
                    nabo += 1

            if nabo > len(bruk)/2: #Hvis man har bommet på tastaturet med halvparten av bokstavene, settes likhet lik 0
                print("Fjernet:", bruk)
                likhet = 0

            nabo = 0

            ord = ""
            for bokstav in bruk:
                if bokstav != "§":
                    ord += bokstav
            sjekket[ord] = likhet
            likhet = 0

        print("Basert på søk:", input)
        #muligeListe = [] #ANDRE ORD SOM LIGNER
        storst = 0
        storstNokkel = ""
        prosent = 0
        for nokkel in sjekket:
            if sjekket[nokkel] > storst:
                storst = sjekket[nokkel]
                storstNokkel = nokkel
        #    if (sjekket[nokkel]/(len(storstNokkel)+1))*100 > 40: #ANDRE ORD SOM LIGNER
        #        muligeListe.append(nokkel) #ANDRE ORD SOM LIGNER
        prosent = str((storst/(len(storstNokkel)+1))*100)
    #    if len(muligeListe) > 0: #ANDRE ORD SOM LIGNER
        #    print(storstNokkel)
        #    muligeListe.remove(storstNokkel) #ANDRE ORD SOM LIGNER
        if storstNokkel.title() in liste:
            print("Funnet:", storstNokkel.title() + ",", prosent + "% lik")
        #    if len(muligeListe) > 1: #ANDRE ORD SOM LIGNER
        #        print("Andre ord som ligner:", muligeListe) #ANDRE ORD SOM LIGNER
            return storstNokkel.title()
        if storstNokkel.upper() in liste:
            print("Funnet:", storstNokkel.upper() + ",", prosent + "% lik")
            #if len(muligeListe) > 1: #ANDRE ORD SOM LIGNER
            #    print("Finner du ordet ditt her?:", muligeListe) #ANDRE ORD SOM LIGNER
            return storstNokkel.upper()



#Hentet og modifisert fra den som funker i Ord
    def _sorter(self):
        nokler = []
        verdi = []
        for glose in self._kategorier:
            nokler.append(glose)
            nokler.sort()

        for glose in self._kategorier:
            index = nokler.index(glose)
            verdi.insert(index, self._kategorier[glose])

        self._kategorier = {}
        for i in range(len(nokler)):
            self._kategorier[nokler[i]] = verdi[i]

    def _lesfil(self, filnavn):
        fil = open(filnavn, "r", encoding = "utf-8")
        for linje in fil:
            delt = linje.strip().split(" | ") #Splitter på |
            kategori = delt[0]
            glose = delt[1]
            forklaring = delt[2]

            if kategori in self._kategorier:
                objekt = self._kategorier[kategori]
                objekt.leggTil(glose, forklaring)
            else:
                objekt = Ord()
                self._kategorier[kategori] = objekt
                objekt.leggTil(glose, forklaring)
        fil.close()

    def _hopp(self):
        for i in range(50):
            print()

class Ord():
    def __init__(self):
        self._ordbok = {}

    def leggTil(self, ord, forklaring):
        self._ordbok[ord] = forklaring

        self._sorter()

    def sok(self, input):
        if input in self._ordbok:
            print(input, "-", self._ordbok[input])
            return(True)

    def skrivUt(self):
        for glose in self._ordbok:
            print()
            print(glose, "-", self._ordbok[glose])

    def _sorter(self):
        nokler = []
        verdi = []
        for glose in self._ordbok:
            nokler.append(glose)
            nokler.sort()

        for glose in self._ordbok:
            index = nokler.index(glose)
            verdi.insert(index, self._ordbok[glose])

        self._ordbok = {}
        for i in range(len(nokler)):
            self._ordbok[nokler[i]] = verdi[i]

def hovedprogram():
    gloser = Kategori("gloseBok.txt")

    print("0 - Avslutt")
    print("1 - Skriv ut hele ordboken")
    print("'Tekst' - Vi søker opp ordet (Kategori eller oppslagsord)")
    valg = input("\nSøk: ")

    if valg == "cls" or valg == "0":
        valg = "0"

    while valg != "0":
        print(valg)
        if valg == "1":
            gloser.skrivUt()
        else:
            gloser.sok(valg)
        print()
        print()
        print("0 - Avslutt")
        print("1 - Skriv ut hele ordboken")
        print("'Tekst' - Vi søker opp ordet (Kategori eller oppslagsord)")
        valg = input("\nSøk: ")
        if valg == "cls" or valg == "0":
            valg = "0"

hovedprogram()
