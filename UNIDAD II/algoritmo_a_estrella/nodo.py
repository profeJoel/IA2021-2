class nodo:

    def __init__(self, x, y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.caminos = []

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_nombre(self):
        return self.nombre
    
    def get_camino(self, indice):
        return self.caminos[indice]

    def get_caminos(self):
        return self.caminos

    def set_camino(self, nuevo):
        self.caminos.append(nuevo)

    def __eq__(self, otro):
        if otro == None:
            return False
        #Consideramos que si el punto está en la misma coordenada, entonces es el mismo punto
        return self.x == otro.get_x() and self.y == otro.get_y()

    def __str__(self):
        """[A (-3,4)]"""
        return "[" + self.nombre + " (" + str(self.x) + "," + str(self.y) + ")]"