from Grafo import Grafo
from itertools import permutations
from typing import Tuple

class GrafoDenso(Grafo):
    def __init__(self, rotulos: int | list):
        if isinstance(rotulos, int):
            self.rotulos = list(range(rotulos))
        elif isinstance(rotulos, list):
            self.rotulos = rotulos.copy()
        else:
            raise ValueError(f"Rotulo inválido. {type(rotulos)}")
        
        self.n = len(self.rotulos)
        self.matriz = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.arestas = 0

    def numero_de_vertices(self):
        return self.n

    def numero_de_arestas(self):
        return self.arestas

    def sequencia_de_graus(self):
        graus = sorted([sum(linha) for linha in self.matriz])
        return graus

    def adicionar_aresta(self, u, v):
        i = self.rotulos.index(u)
        j = self.rotulos.index(v)

        if self.matriz[i][j] == 0:
            self.matriz[i][j] = 1
            self.matriz[j][i] = 1
            self.arestas += 1

    def remover_aresta(self, u, v):
        i = self.rotulos.index(u)
        j = self.rotulos.index(v)

        if self.matriz[i][j] == 1:
            self.matriz[i][j] = 0
            self.matriz[j][i] = 0
            self.arestas -= 1

    def imprimir(self):
        print("Matriz de adjacência: ")
        print(" ", " ".join(map(str, self.rotulos)))
        for i in range(self.n):
            print(self.rotulos[i], " ".join(map(str, self.matriz[i])))

    def is_simples(self):
        is_simples = True
        for i in range(self.n):
            if self.matriz[i][i] == 1:
                is_simples = False
        return is_simples

    def is_nulo(self):
        is_nulo = True
        for i in range(self.n):
            for j in range(self.n):
                if self.matriz[i][j] == 1:
                    is_nulo = False
        return is_nulo
        
    def is_completo(self):
        is_completo = True
        for i in range(self.n):
            for j in range(self.n):
                if self.matriz[i][j] == 0 and i != j:
                    is_completo = False
        return is_completo
    
    def get_vertices(self):
        return self.rotulos.copy()

    def get_arestas(self):
        arestas = []
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.matriz[i][j] == 1:
                    arestas.append((self.rotulos[i], self.rotulos[j]))
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
        meus_vertices = self.get_vertices()
        outros_vertices = outro_grafo.get_vertices()
        if sorted(meus_vertices) != sorted(outros_vertices):
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

        minhas_arestas = self.get_arestas()
        if sorted(minhas_arestas) != sorted(arestas_outro):
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
            print(cores)
            # print(f'{vertice}:')
            cor = 0
            v_adj = []
            for v in vertices:
                if (vertice, v) in arestas or (v, vertice) in arestas:
                    v_adj.append(v)
            
            # print(f'  {v_adj}')
            
            sair = True
            while sair:
                for u in v_adj:
                    if cores[u] == cor:
                        cor += 1
                        break
                else:
                    sair = False

            cores[vertice] = cor

        return (max(cores.values()) + 1, cores)