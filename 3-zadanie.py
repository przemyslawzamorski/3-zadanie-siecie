from nltk.compat import raw_input
from quicksort import quickSort

__author__ = 'przemyslaw zamorski'
'PRogram tworzący minimalne drzewo rozpiętości'




wierzchołki=raw_input("Wprowadz liczbę wierzchołków: ")
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





