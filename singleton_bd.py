class BaseDeDatos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Conectando a la base de datos... Conexión exitosa!")
            cls._instancia = super().__new__(cls)
        return cls._instancia

# --- PRUEBA DEL CÓDIGO ---
conexion_ventas = BaseDeDatos()
conexion_empleados = BaseDeDatos()

print("¿Ambas variables usan la misma conexión? ", conexion_ventas is conexion_empleados)