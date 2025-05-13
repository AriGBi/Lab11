from dataclasses import dataclass

from model.prodotti import Prodotto


@dataclass
class Edge:
    nodoP: Prodotto
    nodoA: Prodotto
    peso: int

    def __hash__(self):
        return hash((self.nodoP,self.nodoA))

    def __eq__(self,other):
        return self.nodoA==other.nodoA and self.nodoP==other.nodoP


    def __str__(self):
        return f"Arco da {self.nodoP.Product_number} a {self.nodoA.Product_number} peso= {self.peso}"

