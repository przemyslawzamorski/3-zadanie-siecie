from nltk.compat import raw_input

__author__ = 'przemyslaw zamorski'
'PRogram tworzący minimalne drzewo rozpiętości'




wierzchołki=raw_input("Wprowadz liczbę wierzchołków: ")
ilość_krawędzi=raw_input("Wprowadz liczbę krawędzi: ")


def lista_krawędzi():
    wagi_krawędzi = raw_input("Wprowadz wagi krwaędzi po spacji: ")
    wagi_krawędzi = wagi_krawędzi.split() #splits the input string on spaces
    wagi_krawędzi = [int(a) for a in wagi_krawędzi]
    if int(len(wagi_krawędzi))==int(ilość_krawędzi):
        return wagi_krawędzi
    else:
        print('wprowadzono niepoprawna liczbę wag krawędzi')
        return False
#wprowadzenie wag krawędzi
wagi_krawędzi=lista_krawędzi()
while (wagi_krawędzi==False):
    wagi_krawędzi=lista_krawędzi()

