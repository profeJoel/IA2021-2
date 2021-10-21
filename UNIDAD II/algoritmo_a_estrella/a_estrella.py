from collections import deque
import sys, os, math
from time import sleep

from nodo import nodo
from arco import arco
from grafo import grafo
from estado import estado

sys.setrecursionlimit(500000)

def ordenar_por_f(e):
    return e.get_f()

def ordenar_por_h(e):
    return e.get_h()

def ordenar_por_g(e):
    return e.get_g()

class busqueda:
    def __init__(self, nodo_inicial, nodo_final, archivo_grafo):
        self.tablero = grafo(archivo_grafo)
        self.estado_inicial = estado(self.tablero.buscar_nodo(nodo_inicial), None, "Inicial", 0)
        self.estado_final = estado(self.tablero.buscar_nodo(nodo_final), None, "Final", None)

        self.estado_inicial.set_g(self.estado_inicial,0)
        self.estado_inicial.set_h(self.estado_final)

        self.estado_actual = None
        self.historial = []
        self.cola_estados = deque()

    def add(self, e):
        self.cola_estados.append(e)
        self.historial.append(e)

    def pop(self):
        return self.cola_estados.popleft()

    def esta_en_historial(self, e):
        return e in self.historial

    def es_final(self):
        return self.estado_actual == self.estado_final

    def mover(self, sucesor):
        destino = sucesor.get_destino()
        nuevo_estado = estado(destino, self.estado_actual, "De " + self.estado_actual.get_estado().get_nombre() + " hasta " + destino.get_nombre(), self.estado_actual.get_nivel() + 1)
        return nuevo_estado

    def buscar_padre(self, e):
        if e.get_padre() == None:
            print(e)
        else:
            padre = e.get_padre()
            self.buscar_padre(padre)
            print(e)

    def traspasar_a_cola(self, lista, N):
        for e in lista:
            self.add(e)
        for n in range(0,N):
            self.cola_estados.appendleft(self.cola_estados.pop())

    def algoritmo_a_estrella(self, inicial, i):
        self.estado_actual = inicial
        cola_transitoria = []

        if self.es_final():
            self.buscar_padre(inicial)
            print("Algoritmo A* Llega a Solucion")
            print("Historial: " + str(len(self.historial)))
            print("Cola Estados: " + str(len(self.cola_estados)))
            print("Iteraciones: " + str(i))
            print("Coste Total: " + str(self.estado_actual.get_f()))
        else:
            sucesores = self.estado_actual.get_sucesores()
            N = 0
            for sucesor in sucesores:
                estado_temporal = self.mover(sucesor)
                if not self.esta_en_historial(estado_temporal):
                    estado_temporal.set_g(self.estado_actual, sucesor.get_coste())
                    estado_temporal.set_h(self.estado_final)
                    cola_transitoria.append(estado_temporal)
                    N += 1
            
            cola_transitoria.sort(key=ordenar_por_f)
            self.traspasar_a_cola(cola_transitoria, N)

            return self.algoritmo_a_estrella(self.pop(), i + 1)

    def busqueda_avara(self, inicial, i):
        self.estado_actual = inicial
        cola_transitoria = []

        if self.es_final():
            self.buscar_padre(inicial)
            print("Algoritmo A* Llega a Solucion")
            print("Historial: " + str(len(self.historial)))
            print("Cola Estados: " + str(len(self.cola_estados)))
            print("Iteraciones: " + str(i))
            print("Coste Total: " + str(self.estado_actual.get_f()))
        else:
            sucesores = self.estado_actual.get_sucesores()
            N = 0
            for sucesor in sucesores:
                estado_temporal = self.mover(sucesor)
                if not self.esta_en_historial(estado_temporal):
                    estado_temporal.set_g(self.estado_actual, 0) # obliga que el coste acumulado sea 0
                    estado_temporal.set_h(self.estado_final)
                    cola_transitoria.append(estado_temporal)
                    N += 1
            
            cola_transitoria.sort(key=ordenar_por_h)
            self.traspasar_a_cola(cola_transitoria, N)

            return self.busqueda_avara(self.pop(), i + 1)

    def busqueda_uniforme(self, inicial, i):
        self.estado_actual = inicial
        cola_transitoria = []

        if self.es_final():
            self.buscar_padre(inicial)
            print("Algoritmo A* Llega a Solucion")
            print("Historial: " + str(len(self.historial)))
            print("Cola Estados: " + str(len(self.cola_estados)))
            print("Iteraciones: " + str(i))
            print("Coste Total: " + str(self.estado_actual.get_f()))
        else:
            sucesores = self.estado_actual.get_sucesores()
            N = 0
            for sucesor in sucesores:
                estado_temporal = self.mover(sucesor)
                if not self.esta_en_historial(estado_temporal):
                    estado_temporal.set_g(self.estado_actual, sucesor.get_coste())
                    estado_temporal.set_h(0) # no se considera
                    cola_transitoria.append(estado_temporal)
                    N += 1
            
            cola_transitoria.sort(key=ordenar_por_g)
            self.traspasar_a_cola(cola_transitoria, N)

            return self.busqueda_uniforme(self.pop(), i + 1)

    def init(self):
        self.add(self.estado_inicial)
        #self.algoritmo_a_estrella(self.pop(),1)
        #self.busqueda_avara(self.pop(),1)
        self.busqueda_uniforme(self.pop(),1)