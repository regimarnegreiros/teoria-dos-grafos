from GrafoDenso import GrafoDenso
from GrafoEsparso import GrafoEsparso

vertices = ['A', 'B', 'C', 'D', 'E']

e = [('A', 'B'), ('A', 'C'), ('C', 'D'), ('C', 'E'), ('B', 'D')]
g1 = GrafoEsparso(vertices)

for u, v in e:
    g1.adicionar_aresta(u, v)

def usar_funções(f: GrafoDenso | GrafoEsparso) -> None:
    print("Número de vértices:", f.numero_de_vertices())
    print("Número de arestas:", f.numero_de_arestas())
    print("Sequência de graus:", f.sequencia_de_graus())
    print("É simples? ", f.is_simples())
    print("É nulo? ", f.is_nulo())
    print("É completo? ", f.is_completo())
    print("Vértices =", f.get_vertices())
    print("Arestas =", f.get_arestas())
    f.imprimir()
    print()

g1.remover_aresta('A', 'C')

print("===== Grafo 1 =====")
usar_funções(g1)

g2 = GrafoEsparso(vertices)
print("===== Grafo 2 =====")
usar_funções(g2)

g3 = GrafoDenso(vertices)
for i in vertices:
    for j in vertices:
        g3.adicionar_aresta(i, j)

print("===== Grafo 3 =====")
usar_funções(g3)

g4 = GrafoDenso(vertices)
for i in vertices:
    for j in vertices:
        if i != j:
            g4.adicionar_aresta(i, j)

print("===== Grafo 4 =====")
usar_funções(g4)


g5 = GrafoEsparso(vertices)
g5.adicionar_aresta('A', 'B')

g6 = GrafoEsparso(vertices)
g6.adicionar_aresta('A', 'B')
g6.adicionar_aresta('B', 'D')

g7 = GrafoDenso(['A', 'B', 'C'])
g7.adicionar_aresta('A', 'B')
g7.adicionar_aresta('A', 'C')

print("===== Grafo 5 =====")
usar_funções(g5)
print("===== Grafo 6 =====")
usar_funções(g6)
print("===== Grafo 7 =====")
usar_funções(g7)


print("===== Testes Subgrafo =====")
print("g6 é subgrafo de g1?", g6.is_subgrafo(g1))
print("g1 é subgrafo de g6?", g1.is_subgrafo(g6))
print("g5 é subgrafo de g4?", g5.is_subgrafo(g4))

print("\n===== Testes Subgrafo Gerador =====")
print("g6 é subgrafo gerador de g1?", g6.is_subgrafo_gerador(g1))
print("g5 é subgrafo gerador de g4?", g5.is_subgrafo_gerador(g4))
print("g7 é subgrafo gerador de g1?", g7.is_subgrafo_gerador(g1))

print("\n===== Testes Subgrafo Induzido =====")
print("g7 é subgrafo induzido de g1?", g7.is_subgrafo_induzido(g1))
print("g5 é subgrafo induzido de g4?", g5.is_subgrafo_induzido(g4))
print("g6 é subgrafo induzido de g1?", g6.is_subgrafo_induzido(g1))

