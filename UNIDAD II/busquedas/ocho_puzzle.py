from nodo import nodo_estado
from collections import deque

class ocho_puzzle:
    estado_final = [nodo_estado("12345678H", None, "Final", None), nodo_estado("1238H4765", None, "Final", None)]
    def __init__(self, EI):
        self.estado_inicial = nodo_estado(EI, None, "Origen", 0)
        self.estado_actual = None
        self.historial = []
        self.cola_estados = deque()
    
    def es_final(self):
        return self.estado_actual in self.estado_final

    def esta_en_historial(self, e):
        return e in self.historial

    def mostrar_estado_actual(self):
        print("Estado Actual\n")
        print("["+str(self.estado_actual.get_nivel())+"]\n")
        print(self.estado_actual.get_estado()[:3]+"\n"+self.estado_actual.get_estado()[3:6]+"\n"+self.estado_actual.get_estado()[6:]+"\n")
    
    def mostrar_estado(self, e):
        print("Estado Actual\n")
        print("["+str(e.get_nivel())+"]\n")
        print(e.get_estado()[:3]+"\n"+e.get_estado()[3:6]+"\n"+e.get_estado()[6:]+"\n")

    def mover_a(self, direccion):
        posicion_espacio = self.estado_actual.get_estado().find("H")

        if direccion == "UP":
            if posicion_espacio < 3:
                return "illegal"
            else:
                aux = self.estado_actual.get_estado()[posicion_espacio-3] # nueva posicion del espacio # -3 se refiere a que se mueve hacia arriba en el string
        
        if direccion == "DOWN":
            if posicion_espacio > 5:
                return "illegal"
            else:
                aux = self.estado_actual.get_estado()[posicion_espacio+3]# +3 se refiere a que se mueve hacia abajo en el string
        
        if direccion == "LEFT":
            if posicion_espacio in [0,3,6]:
                return "illegal"
            else:
                aux = self.estado_actual.get_estado()[posicion_espacio-1]# -1 se refiere a que se mueve hacia la izquierda en el string
            
        if direccion == "RIGHT":
            if posicion_espacio in [2,5,8]:
                return "illegal"
            else:
                aux = self.estado_actual.get_estado()[posicion_espacio+1]# +1 se refiere a que se mueve hacia la derecha en el string

        nuevo_estado = self.estado_actual.get_estado().replace("H","#")
        nuevo_estado = nuevo_estado.replace(aux, "H")
        nuevo_estado = nuevo_estado.replace("#", aux)
        return nuevo_estado

    def buscar_padres(self, e):
        if e.get_padre() == None: # llegamos al nodo origen
            print("\n" + e.get_accion() + "\n Nivel: 0")
            self.mostrar_estado(e)
        else:
            self.buscar_padres(e.get_padre())
            print("\n" + e.get_accion() + "\n Nivel: " + str(e.get_nivel()))
            self.mostrar_estado(e)
        

    def algoritmo_anchura(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.historial.append(self.estado_actual)
        #movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        movimientos = ["DOWN", "UP", "RIGHT", "LEFT"]

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover_a(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_estado() == "illegal" and not self.esta_en_historial(estado_temporal):
                    self.cola_estados.append(estado_temporal)
                    self.historial.append(estado_temporal)
            
            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola: " + str(len(self.cola_estados)))

            self.estado_actual = self.cola_estados.popleft()
            #self.historial.append(self.estado_actual)
            iteracion += 1
        
        print("Iteraciones: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("Hemos llegado a la Solución!!!")

        self.buscar_padres(self.estado_actual)
        print("Resumen Algoritmo en Anchura\n")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola: " + str(len(self.cola_estados)))
        print("Iteraciones: " + str(iteracion) + "\n")

    def add_profundidad(self, pila_sucesores):
        while pila_sucesores.__len__() > 0:
            e = pila_sucesores.pop()
            self.cola_estados.appendleft(e)
            self.historial.append(e)

    def algoritmo_profundidad(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.historial.append(self.estado_actual)
        #movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        movimientos = ["DOWN", "UP", "RIGHT", "LEFT"]
        sucesores = deque()

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover_a(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_estado() == "illegal" and not self.esta_en_historial(estado_temporal):
                    #self.cola_estados.append(estado_temporal)
                    sucesores.append(estado_temporal)
            
            self.add_profundidad(sucesores)
            
            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola: " + str(len(self.cola_estados)))

            self.estado_actual = self.cola_estados.popleft()
            #self.historial.append(self.estado_actual)
            iteracion += 1
        
        print("Iteraciones: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("Hemos llegado a la Solución!!!")

        self.buscar_padres(self.estado_actual)
        print("Resumen Algoritmo en Anchura\n")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola: " + str(len(self.cola_estados)))
        print("Iteraciones: " + str(iteracion) + "\n")
