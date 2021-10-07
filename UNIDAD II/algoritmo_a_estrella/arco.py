from nodo import nodo

class arco:
    def __init__(self, origen, destino, coste):
        self.origen = origen
        self.destino = destino
        self.coste = coste

    def get_origen(self):
        return self.origen

    def get_destino(self):
        return self.destino

    def get_coste(self):
        return self.coste

    def __eq__(self, otro):
        if otro == None:
            return False
        #Si el arco tiene el mismo origen y destino, entonces es el mismo arco
        return self.origen == otro.get_origen() and self.destino == otro.get_destino()
    
    def __str__(self):
        """|ORIGEN| -> coste -> |destino|"""
        return "|" + str(self.origen) + "| -> " + self.coste + " -> |" + str(self.destino) + "|"