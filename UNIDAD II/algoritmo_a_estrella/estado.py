from nodo import nodo
from arco import arco
from grafo import grafo

import math

class estado:
    def __init__(self, nodo, padre, accion, nivel):
        self.valor = nodo
        self.padre = padre
        self.accion = accion
        self.nivel = nivel
        self.g = -1
        self.h = -1

    def get_estado(self):
        return self.valor

    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion

    def get_nivel(self):
        return self.nivel

    def get_sucesores(self):
        return self.valor.get_caminos()

    def get_g(self):
        return self.g
    
    def get_h(self):
        return self.h

    def get_f(self):
        return (self.g + self.h)

    def set_g(self, e, coste):
        """calcula el menor coste desde el estado inicial hasta el estado actual"""
        if e is None:
            self.g = -1
        else:
            g_acumulado = e.get_g() if e.get_g() > 0 else 0
            self.g = g_acumulado + coste # se basa en la acumulación del coste recorrido
    
    def set_h(self, e):
        """h(e) es una estimacion del coste entre el estado actual y el estado final"""
        if e is None:
            self.h = -1

        elif type(e) == int and e == 0:
            self.h = 0 

        else:
            objetivo = e.get_estado()
            #la distancia entre el estado actual y el estado e
            self.h = math.sqrt((objetivo.get_y() - self.valor.get_y())**2 + (objetivo.get_x() - self.valor.get_x())**2)

    def __eq__(self, otro):
        if otro is None:
            return False
        
        return self.valor == otro.get_estado() # comparación de nodos del grafo

    def __str__(self):
        return "Estado " + str(self.valor) + "\nAccion:\n" + self.accion + "\nNivel: " + str(self.nivel) + "\ng(e): " + str(self.g) + "\nh(e): " + str(self.h) + "\nf(e): " + str(self.g + self.h) + "\n" 