from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._colori = DAO.getAllColor()
        self._graph = nx.Graph()
        self._coloreScelto=None
        self._listaProdotti = []
        self._idMap = {}
        self._edges=[]


    def build_Graph(self,colore,anno):
        self._coloreScelto = colore
        self._listaProdotti = DAO.getAllProdotticonCOLORE(colore)
        for p in self._listaProdotti:
            self._idMap[p.Product_number] = p

        self._graph.add_nodes_from(self._listaProdotti)
        self._edges=DAO.getAllEdges(colore,anno,self._idMap)
        for edge in self._edges:
            self._graph.add_edge(edge.nodoP,edge.nodoA, weight=edge.peso)

        return self._graph


    def archiMax(self):
        lista1=self._edges
        finali=[]
        arco1=self.cercaMassimo(lista1)
        lista1.remove(arco1)
        finali.append(arco1)
        arco2 = self.cercaMassimo(lista1)
        lista1.remove(arco2)
        finali.append(arco2)
        arco3=self.cercaMassimo(lista1)
        finali.append(arco3)
        nodiRipetuti=self.cercaRipetuti(finali)
        return finali,nodiRipetuti

    def cercaRipetuti(self,lista):
        nodi=[]
        for arco in lista:
            nodi.append(arco.nodoP)
            nodi.append(arco.nodoA)
        finali=[]
        for nodo in nodi:
           conto=nodi.count(nodo)
           if conto>1 and nodo.Product_number not in finali:
               finali.append(nodo.Product_number)

        return finali








    def cercaMassimo(self,lista):
        pesoAttuale=-1
        arcoMassimo=None
        for edge in lista:
            if edge.peso>pesoAttuale:
                pesoAttuale=edge.peso
                arcoMassimo=edge
        return arcoMassimo














