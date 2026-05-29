# Estrategia 1
class Sumar:
    def ejecutar(self, a, b):
        return a + b

# Estrategia 2
class Restar:
    def ejecutar(self, a, b):
        return a - b

# Clase principal
class Calculadora:
    def __init__(self, estrategia):
        self.estrategia = estrategia # Le decimos qué estrategia usar

    def calcular(self, a, b):
        return self.estrategia.ejecutar(a, b)

# --- PRUEBA DEL CÓDIGO ---
mi_calculadora = Calculadora(Sumar())
print("Resultado de sumar 10 y 5: ", mi_calculadora.calcular(10, 5))

# Cambiamos la estrategia sobre la marcha
mi_calculadora.estrategia = Restar()
print("Resultado de restar 10 y 5: ", mi_calculadora.calcular(10, 5))