class Logger:
    _unica_instancia = None

    def __new__(cls):
     
        if cls._unica_instancia is None:
            print("Creando el sistema de registro (Logger) por primera vez...")
            cls._unica_instancia = super().__new__(cls)
        return cls._unica_instancia

    def registrar(self, mensaje):
        print(f"[REGISTRO]: {mensaje}")

# --- PRUEBA DEL CÓDIGO ---
logger1 = Logger()
logger2 = Logger()

# Usamos el logger
logger1.registrar("El programa ha iniciado.")
logger2.registrar("El usuario hizo clic en el botón.")

# Comprobamos si realmente son el mismo objeto (solo hay 1 en memoria)
print("¿logger1 y logger2 son exactamente el mismo? ", logger1 is logger2)