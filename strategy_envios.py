class EnvioNormal:
    def coste(self, peso):
        return peso * 2  # 2 euros por kilo

class EnvioExpres:
    def coste(self, peso):
        return peso * 5  # 5 euros por kilo

class Tienda:
    def __init__(self, estrategia_envio):
        self.estrategia_envio = estrategia_envio

    def calcular_envio(self, peso):
        coste_total = self.estrategia_envio.coste(peso)
        print(f"El coste del envío será de {coste_total} euros.")

# --- PRUEBA DEL CÓDIGO ---
paquete_kilos = 10

tienda = Tienda(EnvioNormal())
tienda.calcular_envio(paquete_kilos)

# El cliente tiene prisa, cambiamos a Exprés
tienda.estrategia_envio = EnvioExpres()
tienda.calcular_envio(paquete_kilos)