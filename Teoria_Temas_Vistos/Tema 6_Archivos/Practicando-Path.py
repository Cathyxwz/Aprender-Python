from pathlib import Path

# 1. Obtener el directorio principal del ordenador (ejemplo: C:\Users\kathe)
base = Path.home()

# 2. Construir una ruta a partir de strings
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada familia.txt"))
print(guia)
# Resultado: C:\Users\kathe\Europa\España\Barcelona\Sagrada familia.txt

# 3. Cambiar el nombre del archivo dentro de la misma ruta
guia2 = guia.with_name("La Pedrera.txt")
print(guia2)
# Resultado: C:\Users\kathe\Europa\España\Barcelona\La Pedrera.txt

# 4. Buscar archivos dentro de una carpeta con patrón (glob)
guia3 = Path(Path.home() / "Europa")
for txt in Path(guia3).glob("**/*.txt"):   # el patrón **/*.txt busca todos los .txt en subcarpetas
    print(txt)

# 5. Usar relative_to para obtener la ruta relativa
guia4 = Path("Europa", "España", "Barcelona")

en_europa = guia4.relative_to(Path("Europa"))
print(en_europa)   # Resultado: España\Barcelona

en_españa = guia4.relative_to(Path("Europa", "España"))
print(en_españa)   # Resultado: Barcelona
