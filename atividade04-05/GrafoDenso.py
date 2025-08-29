from Grafo import Grafo

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
        graus = [sum(linha) for linha in self.matriz]
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