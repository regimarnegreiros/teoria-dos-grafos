from GrafoEsparso import GrafoEsparso

materias = ['M', 'A', 'C', 'F', 'Q', 'P']
g = GrafoEsparso(materias)

g.adicionar_aresta('C', 'F')
g.adicionar_aresta('C', 'A')
g.adicionar_aresta('F', 'A')
g.adicionar_aresta('M', 'P')
g.adicionar_aresta('M', 'A')
g.adicionar_aresta('P', 'A')
g.adicionar_aresta('Q', 'F')

for v_origin, v_dest in g.get_arestas():
    print(f'- Aula {v_origin} tem conflito com: {v_dest}')
print('-' * 30)


# print("Número de vértices:", g.numero_de_vertices())
# print("Número de arestas:", g.numero_de_arestas())
# print("Sequência de graus:", g.sequencia_de_graus())
# print("É simples? ", g.is_simples())
# print("É nulo? ", g.is_nulo())
# print("É completo? ", g.is_completo())
# print("Vértices =", g.get_vertices())
# print("Arestas =", g.get_arestas())
# g.imprimir()
# print()

numero_minimo_horarios, cores_atribuidas = g.colorir_grafo()
print('Número mínimo de horários necessários:', numero_minimo_horarios)
print('Cores atribuídas:', cores_atribuidas)