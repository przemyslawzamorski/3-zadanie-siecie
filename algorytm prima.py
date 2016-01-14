from collections import defaultdict
from heapq import *
from nltk.compat import raw_input
from quicksort import quickSort

##wprowadzanie danych
# wierzchołki=raw_input("Wprowadz wierzchołki: ")
# wierzchołki=wierzchołki.split()
# lista_wierzchołkow= [(a) for a in wierzchołki]
# print(lista_wierzchołkow)
#
# ilość_krawędzi=raw_input("Wprowadz liczbę krawędzi: ")
# lista_krawedzi=[]
# #dodawanie krawedzi
# for x in range(0,int(ilość_krawędzi)):
#     krawedz= raw_input("Wprowadz 2 wierzchołki krawedzi i wage kazde po spacji nastepnie enter: ")
#     krawedz= krawedz.split()
#     krawedz= [(a) for a in krawedz]
#     lista_krawedzi.append(krawedz)
#
# #sortowanie
# lista_krawedzi=quickSort(lista_krawedzi)
# print(lista_krawedzi)
#


lista_wierzchołkow = list("ABCDEFG")
lista_krawedzi = [ ("A", "B", 7), ("A", "D", 5),
          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
      ("C", "E", 5),
      ("D", "E", 15), ("D", "F", 6),
      ("E", "F", 8), ("E", "G", 9),
      ("F", "G", 11)]



##prim
def prim( nodes, edges ):
    #dict list zawierający jeden wierzchołek i jedgo odwołanie do innego tworząc z nim krawedz o podanej wadze
    zbiór_punktów_z_odcinkaki = defaultdict( list )

    for w1,w2,w in edges:
        zbiór_punktów_z_odcinkaki[ w1 ].append( (w, w1, w2) )
        zbiór_punktów_z_odcinkaki[ w1 ].append( (w, w2, w1) )


    minimalne_drzewo = []
    #wybieram jeden wierzchołek początkowy
    użyte_wierzchołki = set( nodes[ 0 ] )
    # z wszystkich odcinków wybieramy te zawierające wybrany wierzchołek
    możliwe_do_użycia = zbiór_punktów_z_odcinkaki[ nodes[0] ][:]

    #sortujemy je według wagi od najniższej do najwyższej
    heapify( możliwe_do_użycia )

    # w przypadku gdy mamy krawedzie do uzycia wykonujemy algorytm
    while możliwe_do_użycia:
        #bierzemy najnisze ze względu na koszt krawedz z mozliwych do uzycia
        cost, n1, n2 = heappop( możliwe_do_użycia )


        if n2 not in użyte_wierzchołki:
            #jeżeli drugi koniec nie znajduje sie juz  w uzyciu bierzemy go i wrzucamy do uzytych wierzcholkow
            użyte_wierzchołki.add( n2 )
            #tak samo umieszczamy go w nimimalnym drzewie
            minimalne_drzewo.append( ( n1, n2, cost ) )

            #dla wszystkich odcinków w grafie zawierajacych drugi koniec przed chwiląa wpisanego
            #odcinka do minimalnego drzewa wyszukujemy  odcinki zawierajace go w sobie
            #a nastepnie sprawdzamy czy jego 2 wierzchołek z którym tworzy odcinek nie jest w użyciu jeżeli
            # nie to dodajemy go do aktualnie mozliwych do użycia
            for e in zbiór_punktów_z_odcinkaki[ n2 ]:
                if e[ 2 ] not in użyte_wierzchołki:
                    heappush( możliwe_do_użycia, e )


    # w przypadku gdy nie mamy krawedzi zwracamy minimalne drzewo
    return minimalne_drzewo
 
#test

 
print ( prim( lista_wierzchołkow, lista_krawedzi ))
