import random
import time

class Entorno:
    def __init__(self, ruta):
        self.ruta = ruta
        self.posicion = 0
    
    def mover(self):
        if self.posicion < len(self.ruta) - 1:
            self.posicion += 1
        else:
            self.posicion = 0  # Volver al inicio cuando llegue al final

    def detectar_obstaculo(self):
        return self.ruta[self.posicion] == "X"  # "X" indica un obstáculo

class Agente:
    def __init__(self, entorno):
        self.entorno = entorno
        self.direccion = 1  # 1 para ir hacia adelante, -1 para ir hacia atrás

    def patrullar(self):
        while True:
            print(f"Posición actual: {self.entorno.posicion}, Dirección: {'Adelante' if self.direccion == 1 else 'Atrás'}")
            if self.entorno.detectar_obstaculo():
                print("¡Obstáculo detectado! Cambiando de dirección...")
                self.direccion *= -1  # Cambiar la dirección aleatoriamente

            self.entorno.mover()
            time.sleep(1)  # Esperar 1 segundo antes de continuar con el siguiente movimiento

            # Cambio de dirección aleatorio para reflejo simple
            if random.random() < 0.1:  # 10% de probabilidad de cambiar dirección aleatoriamente
                self.direccion *= -1

if __name__ == "__main__":
    ruta = [" ", " ", "X", " ", " ", "X", " ", " ", " "]  # Ruta con obstáculos ("X")
    entorno = Entorno(ruta)
    agente = Agente(entorno)
    agente.patrullar()