from a_estrella import busqueda
from nodo import nodo

if __name__ == "__main__":
    origen = nodo(-3.0,4.0,"Origen")
    destino = nodo(-1.0,-3.0, "Destino")

    experimento = busqueda(origen, destino, "grafo1.txt")
    print(experimento.tablero)
    experimento.init()