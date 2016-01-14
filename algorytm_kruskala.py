from operator import itemgetter

##wprowadzanie wierzchołków
from nltk.compat import raw_input
from quicksort import quickSort

wierzchołki=raw_input("Wprowadz wierzchołki: ")
wierzchołki=wierzchołki.split()
lista_wierzchołkow= [(a) for a in wierzchołki]
print(lista_wierzchołkow)

ilość_krawędzi=raw_input("Wprowadz liczbę krawędzi: ")
lista_krawedzi=[]
#dodawanie krawedzi
for x in range(0,int(ilość_krawędzi)):
    krawedz= raw_input("Wprowadz 2 wierzchołki krawedzi i wage kazde po spacji nastepnie enter: ")
    krawedz= krawedz.split()
    krawedz= [(a) for a in krawedz]
    lista_krawedzi.append(krawedz)

#sortowanie
lista_krawedzi=quickSort(lista_krawedzi)
print(lista_krawedzi)

##przykladowe dane

# lista_wierzchołkow = list( "ABCDEF" )
# lista_krawedzi = [ ("A", "B", 4), ("B", "C", 2),
#           ("A", "F", 2),("C", "D", 8),
#           ("F", "D", 6),
#           ("A", "E", 1),("E", "B", 2),
#           ("F", "E", 7),("E", "D", 3),
#           ]


##########
print('algorytm kruskala')

##algorytm pomocny w tworzeniu drzewa
class Tworzenie_lasu(dict):
    def dodaj_wierzchołek(self, item):
        self[item] = item

    def znajdz_wierzchołek(self, item):
        nadrzędny = self[item]

        while self[nadrzędny] != nadrzędny:
            parent = self[nadrzędny]

        self[item] = nadrzędny
        return nadrzędny

    def złącz(self, item1, item2):
        self[item2] = self[item1]



###algorytm kruskala

def kruskal( wierzchołki, krawędzie  ):
    #wczytanie do do kruskala pomocniczej klasy
    las = Tworzenie_lasu()
    #definicja wejsciowego pustego drzewa minimalnego
    minimalne_drzewo = []

    #dodaie do lasu wierzchołków
    for n in wierzchołki:
        las.dodaj_wierzchołek( n )

    #używamy jednego wierzchołka
    dostępne_wierzchołki = len(wierzchołki) - 1
 
    for edge in sorted( krawędzie, key=itemgetter( 2 ) ):
        #podpisanie wierzchołków krawędzi iterujac od najmniejszej
        n1, n2, _ = edge
        tree1 = las.znajdz_wierzchołek(n1)
        tree2 = las.znajdz_wierzchołek(n2)
        #jeżeli sa różnie wierzchołki i łaćzą punkt dodaj do minimalnego drzewa
        if tree1 != tree2:
            minimalne_drzewo.append(edge)
            dostępne_wierzchołki -= 1
            if dostępne_wierzchołki == 0:
                return minimalne_drzewo
         
            las.złącz(tree1, tree2)
 

#test
mdr= (kruskal( lista_wierzchołkow, lista_krawedzi ))
print(mdr)

waga_drzewa=0
for x in mdr:
    waga_drzewa=waga_drzewa+int(x[2])

print('waga drzewa wynosi', waga_drzewa)