from nodo import nodo
from arco import arco

class grafo:
    def __init__(self, archivo_grafo):
        self.nodos = []
        self.arcos = []
        #debemos realizar la lectura y carga del grafo
        self.lee_archivo_grafo(archivo_grafo)

    def get_nodo(self, indice):
        return self.nodos[indice]

    def get_arco(self, indice):
        return self.arcos[indice]

    def nuevo_nodo(self, x, y, nombre):
        nuevo = nodo(x,y,nombre)
        self.nodos.append(nuevo)

    def nuevo_arco(self, origen, destino, coste):
        nuevo = arco(origen, destino, coste)
        origen.set_camino(nuevo)
        self.arcos.append(nuevo)

    def lee_archivo_grafo(self, archivo):

        with open(archivo) as en_archivo:
            for linea in en_archivo:
                posicion = linea.split(' ')
                x1 = float(posicion[0])
                y1 = float(posicion[1])

                auxiliar = nodo(x1, y1, posicion[2])
                if auxiliar in self.nodos:
                    origen = self.nodos[self.nodos.index(auxiliar)] #recuperar la referencia del nodo original
                else:
                    self.nuevo_nodo(x1, y1, posicion[2])
                    origen = self.nodos[self.nodos.index(auxiliar)] #recuperar la referencia del nodo original

                x1 = float(posicion[3])
                y1 = float(posicion[4])

                auxiliar = nodo(x1, y1, posicion[5])
                if auxiliar in self.nodos:
                    destino = self.nodos[self.nodos.index(auxiliar)] #recuperar la referencia del nodo original
                else:
                    self.nuevo_nodo(x1, y1, posicion[5])
                    destino = self.nodos[self.nodos.index(auxiliar)] #recuperar la referencia del nodo original

                coste = float(posicion[6])

                self.nuevo_arco(origen, destino, coste)

    def __str__(self):
        salida = "\nNodos:\n"
        for n in self.nodos:
            salida += str(n) + " = ["
            for c in n.get_caminos():
                salida += str(c) + ", "
            salida += "]\n"

        salida += "\nArcos:\n"
        for a in self.arcos:
            salida += str(a) + "\n"

        return "El grafo es: " + salida

    def buscar_nodo(self, n):
        if n in self.nodos:
            return self.nodos[self.nodos.index(n)]
        else:
            self.nuevo_nodo(n.get_x(), n.get_y(), n.get_nombre())
            return self.nodos[self.nodos.index(n)]

                