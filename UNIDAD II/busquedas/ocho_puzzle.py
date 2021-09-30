from nodo import nodo_estado
from collections import deque

def ordenar_por_heuristica(e):
    return e.get_distancia()

class ocho_puzzle:
    estado_final = [nodo_estado("12345678H", None, "Final", None), nodo_estado("1238H4765", None, "Final", None)]
    def __init__(self, EI):
        self.estado_inicial = nodo_estado(EI, None, "Origen", 0)
        self.calcular_heuristica(self.estado_inicial)
        self.estado_actual = None
        self.historial = []
        self.cola_estados = deque()
    
    def es_final(self):
        return self.estado_actual in self.estado_final

    def esta_en_historial(self, e):
        return e in self.historial

    def mostrar_estado_actual(self):
        print("Estado Actual")
        print("["+str(self.estado_actual.get_nivel())+"]")
        print("Heuristica: " + str(self.estado_actual.get_distancia()))
        print(self.estado_actual.get_estado()[:3]+"\n"+self.estado_actual.get_estado()[3:6]+"\n"+self.estado_actual.get_estado()[6:]+"\n")
    
    def mostrar_estado(self, e):
        print("Estado Actual")
        print("["+str(e.get_nivel())+"]")
        print("Heuristica: " + str(e.get_distancia()))
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
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        #movimientos = ["DOWN", "UP", "RIGHT", "LEFT"]

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
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        #movimientos = ["DOWN", "UP", "RIGHT", "LEFT"]
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

    def espacios_desubicados(self, estado_presente, estado_objetivo):
        """Permite comparar los estados, contando los espacios desubicados"""
        d = 0
        for i in range(len(estado_presente.get_estado())):
            if not estado_presente.get_estado()[i] == estado_objetivo.get_estado()[i]:
                d += 1
        return d

    def calcular_heuristica(self, estado):
        primero = True
        for final in self.estado_final:
            if primero:
                distancia = self.espacios_desubicados(estado, final)
                primero = False
            else:
                nueva_distancia = self.espacios_desubicados(estado, final)

                if nueva_distancia < distancia:
                    distancia = nueva_distancia
        
        estado.set_distancia(distancia)

    def algoritmo_primero_mejor(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.historial.append(self.estado_actual)
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        sucesores = []

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover_a(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_estado() == "illegal" and not self.esta_en_historial(estado_temporal):
                    self.calcular_heuristica(estado_temporal)
                    sucesores.append(estado_temporal)
            
            sucesores.sort(key=ordenar_por_heuristica)
            self.add_profundidad(sucesores)
            
            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola: " + str(len(self.cola_estados)))

            self.estado_actual = self.cola_estados.popleft()
            iteracion += 1
        
        print("Iteraciones: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("Hemos llegado a la Solución!!!")

        self.buscar_padres(self.estado_actual)
        print("Resumen Algoritmo en Primero el Mejor\n")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola: " + str(len(self.cola_estados)))
        print("Iteraciones: " + str(iteracion) + "\n")

    def algoritmo_hill_climbing(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.historial.append(self.estado_actual)
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        sucesores = []
        termina_bien = True

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover_a(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_estado() == "illegal" and not self.esta_en_historial(estado_temporal):
                    self.calcular_heuristica(estado_temporal)
                    sucesores.append(estado_temporal)
            
            sucesores.sort(key=ordenar_por_heuristica)
            self.add_profundidad(sucesores)
            
            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola: " + str(len(self.cola_estados)))

            estado_anterior = self.estado_actual
            self.estado_actual = self.cola_estados.popleft()

            if estado_anterior.get_distancia() < self.estado_actual.get_distancia():
                print("Iteracion: " + str(iteracion) + "\n")
                self.mostrar_estado_actual()
                print("\n\nNO HAY SOLUCION")
                print("Resumen Algoritmo en Primero el Mejor\n")
                print("\nElementos en Historial: " + str(len(self.historial)))
                print("\nElementos en Cola: " + str(len(self.cola_estados)))
                print("Iteraciones: " + str(iteracion) + "\n")
                termina_bien = False
                break

            iteracion += 1

        if termina_bien:
            print("Iteraciones: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()
            print("Hemos llegado a la Solución!!!")

            self.buscar_padres(self.estado_actual)
            print("Resumen Algoritmo en Hill Climbing\n")
            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola: " + str(len(self.cola_estados)))
            print("Iteraciones: " + str(iteracion) + "\n")
        else:
            print("Termina Mal... No hay solucion para este algoritmo")

    def add_beam(self, sucesores, b):
        for estado in sucesores:
            if b > 0:
                self.historial.append(estado)
                self.cola_estados.append(estado)
                b -= 1
            else:
                self.historial.append(estado) #a pesar de no ser un buen estado, debe quedar registrado en el historial como conocido.
    
    def algoritmo_beam(self):
        iteracion = 1
        b = 2 # variable de corte de los sucesores aceptados
        self.estado_actual = self.estado_inicial
        self.historial.append(self.estado_actual)
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        
        sucesores = []

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover_a(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_estado() == "illegal" and not self.esta_en_historial(estado_temporal):
                    self.calcular_heuristica(estado_temporal)
                    sucesores.append(estado_temporal)
            
            sucesores.sort(key=ordenar_por_heuristica)
            self.add_beam(sucesores, b)
            sucesores.clear()
            
            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola: " + str(len(self.cola_estados)))

            self.estado_actual = self.cola_estados.popleft()
            #self.historial.append(self.estado_actual)
            iteracion += 1
        
        print("Iteraciones: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("Hemos llegado a la Solución!!!")

        self.buscar_padres(self.estado_actual)
        print("Resumen Algoritmo Beam\n")
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola: " + str(len(self.cola_estados)))
        print("Iteraciones: " + str(iteracion) + "\n")