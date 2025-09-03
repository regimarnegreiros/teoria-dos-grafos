from Grafo import Grafo
from typing import List, Tuple, Any
from itertools import permutations

class GrafoEsparso(Grafo):
    def __init__(self, rotulos: int | list):
        if isinstance(rotulos, int):
            self.rotulos = list(range(rotulos))
        elif isinstance(rotulos, list):
            self.rotulos = rotulos.copy()
        else:
            raise ValueError(f"Rótulo inválido. {type(rotulos)}")

        self.n = len(self.rotulos)
        self.adj = {v: [] for v in self.rotulos}
        self.arestas = 0

    def numero_de_vertices(self):
        return self.n

    def numero_de_arestas(self):
        return self.arestas

    def sequencia_de_graus(self):
        return sorted([len(self.adj[v]) for v in self.rotulos])

    def adicionar_aresta(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)
            self.adj[v].append(u)
            self.arestas += 1

    def remover_aresta(self, u, v):
        if v in self.adj[u]:
            self.adj[u].remove(v)
            self.adj[v].remove(u)
            self.arestas -= 1

    def imprimir(self):
        print("Lista de adjacência:")
        for v in self.rotulos:
            print(f"{v}: {self.adj[v]}")

    def is_simples(self):
        for v in self.rotulos:
            if v in self.adj[v]:
                return False
        return True

    def is_nulo(self):
        for v in self.rotulos:
            if self.adj[v]:
                return False
        return True

    def is_completo(self):
        for v in self.rotulos:
            if len(self.adj[v]) != self.n - 1:
                return False
        return True

    def get_vertices(self) -> list:
        return self.rotulos.copy()

    def get_arestas(self) -> List[Tuple[Any, Any]]:
        arestas = []
        for u in self.rotulos:
            for v in self.adj[u]:
                if (v, u) not in arestas:
                    arestas.append((u, v))
        return arestas

    def is_subgrafo(self, outro_grafo: Grafo):
        for v in self.rotulos:
            if v not in outro_grafo.get_vertices():
                return False

        arestas_outro = outro_grafo.get_arestas()
        for aresta in self.get_arestas():
            if aresta not in arestas_outro and (aresta[1], aresta[0]) not in arestas_outro:
                return False

        return True

    def is_subgrafo_gerador(self, outro_grafo: Grafo):
        if sorted(self.get_vertices()) != sorted(outro_grafo.get_vertices()):
            return False

        arestas_outro = outro_grafo.get_arestas()
        for aresta in self.get_arestas():
            if aresta not in arestas_outro and (aresta[1], aresta[0]) not in arestas_outro:
                return False

        return True

    def is_subgrafo_induzido(self, outro_grafo: Grafo):
        for v in self.rotulos:
            if v not in outro_grafo.get_vertices():
                return False

        arestas_outro = []
        for (u, v) in outro_grafo.get_arestas():
            if u in self.rotulos and v in self.rotulos:
                arestas_outro.append((u, v))

        if sorted(self.get_arestas()) != sorted(arestas_outro):
            return False

        return True
    
    def is_isomorfo(self, outro_grafo):
        pass

    def is_isomorfo(self, outro_grafo: Grafo):
        if not isinstance(outro_grafo, Grafo):
            raise ValueError(f"Tipo inválido. {type(rotulos)}")
        
        if (self.numero_de_arestas() != outro_grafo.numero_de_arestas()
            or self.numero_de_vertices() != outro_grafo.numero_de_vertices()
            or self.sequencia_de_graus() != outro_grafo.sequencia_de_graus()):
            return False

        vertices_1 = list(self.get_vertices())
        vertices_2 = list(outro_grafo.get_vertices())

        arestas_1 = self.get_arestas()
        arestas_2 = outro_grafo.get_arestas()

        for perm in permutations(vertices_2):
            mapping = dict(zip(vertices_1, perm))

            for aresta in arestas_1:
                u1, v1 = aresta

                u2 = mapping[u1]
                v2 = mapping[v1]

                if not ((u2, v2) not in arestas_2) and ((v2, u2) not in arestas_2):
                    return True
                    
        return False