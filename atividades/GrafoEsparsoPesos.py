from __future__ import annotations
from Grafo import Grafo
from typing import List, Tuple, Any
from itertools import permutations
from typing import Tuple

class GrafoEsparsoComPesos(Grafo):
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

    def adicionar_aresta(self, u, v, peso: float = 1.0):
        if not any(viz == v for viz, _ in self.adj[u]):
            self.adj[u].append((v, peso))
            self.adj[v].append((u, peso))
            self.arestas += 1

    def remover_aresta(self, u, v):
        if any(viz == v for viz, _ in self.adj[u]):
            self.adj[u] = [(viz, p) for viz, p in self.adj[u] if viz != v]
            self.adj[v] = [(viz, p) for viz, p in self.adj[v] if viz != u]
            self.arestas -= 1

    def adicionar_vertice(self, vertice):
        if vertice not in self.rotulos:
            self.rotulos.append(vertice)
            self.adj[vertice] = []
            self.n += 1
        else:
            raise ValueError(f"O vértice {vertice} já existe.")

    def remover_vertice(self, vertice):
        if vertice in self.rotulos:
            # Remover todas as arestas conectadas ao vértice
            for v, p in self.adj[vertice]:
                self.adj[v] = [(viz, p) for viz, p in self.adj[v] if viz != vertice]
                self.arestas -= 1
            
            # Remove o vértice da lista de vértices e do dicionário de adjacências
            self.rotulos.remove(vertice)
            del self.adj[vertice]
            self.n -= 1
        else:
            raise ValueError(f"O vértice {vertice} não existe.")

    def imprimir(self):
        print("Lista de adjacência (com pesos):")
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

    def get_arestas(self) -> List[Tuple[Any, Any, float]]:
        arestas = []
        for u in self.rotulos:
            for v, peso in self.adj[u]:
                if not any((a == v and b == u) for a, b, _ in arestas):
                    arestas.append((u, v, peso))
        return arestas

    def is_subgrafo(self, outro_grafo: Grafo):
        for v in self.rotulos:
            if v not in outro_grafo.get_vertices():
                return False

        arestas_outro = outro_grafo.get_arestas()
        for (u, v, p) in self.get_arestas():
            if not any(
                (a == u and b == v) or (a == v and b == u) for a, b, _ in arestas_outro
            ):
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

                if ((u2, v2) not in arestas_2) and ((v2, u2) not in arestas_2):
                    break
            else:
                return True
                    
        return False

    def colorir_grafo(self) -> Tuple[int, list]:
        vertices = self.get_vertices()
        arestas = self.get_arestas()
        
        cores = {}
        for v in vertices:
            cores[v] = None

        for vertice in vertices:
            cor = 0
            v_adj = []
            for v in vertices:
                if (vertice, v) in arestas or (v, vertice) in arestas:
                    v_adj.append(v)

            while True:
                for u in v_adj:
                    if cores[u] == cor:
                        cor += 1
                        break
                else:
                    break

            cores[vertice] = cor

        return (max(cores.values()) + 1, cores)
    
    def kruskal(self):
        vertices = self.get_vertices()
        arestas = sorted(self.get_arestas(), key=lambda x: x[2])
        floresta = [GrafoEsparsoComPesos([i]) for i in vertices]

        for u, v, p in arestas:
            arvores_a_conectar = []

            # print(*(arv.get_vertices() for arv in floresta))

            for i, arvore in enumerate(floresta):
                arv_v = arvore.get_vertices()
                if (u in arv_v and v in arv_v):
                    break

                if (u in arv_v or v in arv_v):
                    arvores_a_conectar.append(i)

            else:
                arvore_a: GrafoEsparsoComPesos = floresta[arvores_a_conectar[0]]
                arvore_b: GrafoEsparsoComPesos = floresta[arvores_a_conectar[1]]

                for ver in arvore_b.get_vertices():
                    arvore_a.adicionar_vertice(ver)
                    
                for a in arvore_b.get_arestas():
                    arvore_a.adicionar_aresta(*a)
                
                arvore_a.adicionar_aresta(u, v, p)

                floresta[arvores_a_conectar[0]] = arvore_a
                floresta.remove(arvore_b)

        return floresta[0]

                    
if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E']

    e = [
        ('A', 'B', 3), 
        ('A', 'D', 1), 
        ('B', 'C', 5), 
        ('B', 'D', 4), 
        ('C', 'E', 2),
        ('E', 'D', 6)
    ]

    g1 = GrafoEsparsoComPesos(vertices)
    for u, v, p in e:
        g1.adicionar_aresta(u, v, p)

    print('Antes algoritmo Kruskal: ', end='\n\n')
    g1.imprimir()
    print()

    print('Vertices: ', g1.get_vertices())
    print('Arestas: ', g1.get_arestas())
    print('\n')

    g2 = g1.kruskal()
    print('Após o algoritmo Kruskal: ', end='\n\n')
    g2.imprimir()

    print('Vertices: ', g2.get_vertices())
    print('Arestas: ', g2.get_arestas())
