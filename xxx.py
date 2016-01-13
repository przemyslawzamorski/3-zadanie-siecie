from operator import itemgetter

class DisjointSet(dict):
    def add(self, item):
        self[item] = item

    def find(self, item):
        parent = self[item]

        while self[parent] != parent:
            parent = self[parent]

        self[item] = parent
        return parent

    def union(self, item1, item2):
        self[item2] = self[item1]


def kruskal( nodes, edges ):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add( n )
 
    sz = len(nodes) - 1
 
    for e in sorted( edges, key=itemgetter( 2 ) ):
        n1, n2, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            if sz == 0:
                return mst
         
            forest.union(t1, t2)
 
 
#test   
 
nodes = list( "ABCDEF" )
edges = [ ("A", "B", 4), ("B", "C", 2),
          ("A", "F", 2),("C", "D", 8),
          ("F", "D", 6),
          ("A", "E", 1),("E", "B", 2),
          ("F", "E", 7),("E", "D", 3),
          ]
         
print (kruskal( nodes, edges ))

