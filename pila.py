class _Nodo:
    def __init__(self,dato,prox=None):
        self.dato = dato
        self.prox = prox

class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self,dato):
        self.tope = _Nodo(dato,self.tope)

    def desapilar(self):
        
        if self.esta_vacia():
            raise ValueError("Pila vacía")
        
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def ver_tope(self):
        if self.esta_vacia():
            raise ValueError("Pila vacía")
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None 

    def vaciar(self):
        self.tope = None
