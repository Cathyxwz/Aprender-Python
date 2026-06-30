# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) — MÉTODOS ESPECIALES

class CD:
    def __init__(self, autor, titulo, nro_canciones):
        self.autor = autor
        self.titulo = titulo
        self.nro_canciones = nro_canciones

    # __str__ → representación en texto del objeto
    def __str__(self):
        return f"CD {self.autor} de {self.titulo}"

    # __len__ → define qué devuelve len(objeto)
    def __len__(self):
        return self.nro_canciones

    # __del__ → se ejecuta al eliminar el objeto
    def __del__(self):
        print("El CD ha sido eliminado")

# Crear objeto
cd_1 = CD("Pink Floyd", "The wall", 24)

# Usar métodos especiales
print(cd_1)        # usa __str__
print(len(cd_1))   # usa __len__
del cd_1           # usa __del__
