from abc import ABC, abstractmethod

class Grafo(ABC):
    @abstractmethod
    def numero_de_vertices(self):
        """Retorna o número de vértices."""
        pass

    @abstractmethod
    def numero_de_arestas(self):
        """Retorna o número de arestas."""
        pass

    @abstractmethod
    def sequencia_de_graus(self):
        """Retorna a sequência de graus."""
        pass

    @abstractmethod
    def adicionar_aresta(self, u, v):
        """Adiciona uma nova aresta."""
        pass

    @abstractmethod
    def remover_aresta(self, u, v):
        """Remove uma aresta."""
        pass

    @abstractmethod
    def imprimir(self):
        """Imprime a matriz / lista ligada do grafo."""
        pass

    @abstractmethod
    def is_simples(self) -> bool:
        """Retorna se o grafo é simples."""
        pass

    @abstractmethod
    def is_nulo(self) -> bool:
        """Retorna se o grafo é nulo."""
        pass

    @abstractmethod
    def is_completo(self) -> bool:
        """Retorna se o grafo é completo."""
        pass
