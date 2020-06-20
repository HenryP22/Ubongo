import random
import graphviz
class Grafo(object):
    def __init__(self, n):
        self.G = graphviz.Digraph()
        self.n = n
        self.visitados = [False] * n
        self.colores = [None] * n
        self.ruta = [None] * n

    def crear(self):
        gema_list = [1, 2, 3, 4, 5, 6]
        for i in range(self.n):
            m = random.choice(gema_list)
            self.G.node(str(i), str(m))
            self.colores[i] = m

    def conectarTodo(self):
        h = 5
        c = 1
        for i in range(self.n - 6):
            for j in range(6):
                j = (i + h) + c
                self.G.edge(str(i), str(j))
                c = c + 1
                if c == 7:
                    c = 1
            h = h - 1
            if h == -1:
                h = 5

    def tomarGema(self, a, ultimo):
        if self.visitados[a] == False:
            self.G.edge(str(a), str(a + 6))
            self.G.edge(str(ultimo), str(a))
            self.visitados[a] = True
            self.visitados[a + 6] = True
        else:
            return

    def mostrar(self):
        self.G.graph_attr['rankdir'] = 'LR'
        return graphviz.Source(self.G)