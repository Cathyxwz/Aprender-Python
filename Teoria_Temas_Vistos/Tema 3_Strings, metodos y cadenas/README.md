# 📚 Lo que aprendí

- **Indexación y slicing** → acceder a caracteres específicos o extraer sub-strings de un texto.  
- **Métodos de string** → `upper()`, `lower()`, `split()`, `join()`, `find()`, `replace()`.  
- **Propiedades de strings** → concatenar (+), multiplicar (*), triple comillas, `in`, `len()`.  
- **Listas [ ]** → colecciones ordenadas y modificables (`.append()`, `.pop()`, `.sort()`, `.reverse()`).  
- **Diccionarios { }** → pares clave-valor (`.keys()`, `.values()`, `.items()`).  
- **Tuples ( )** → colecciones ordenadas e inmutables (`.count()`, `.index()`).  
- **Sets { }** → colecciones sin repetidos, no ordenadas (`.add()`, `.remove()`, `.union()`).  
- **Booleanos** → `True`/`False` con operadores de comparación (`>`, `==`, `>=`, `!=`).  

---

# 💡 Mini proyecto: Analizador de texto

## 📖 Descripción
El proyecto consistió en crear un programa que analiza un texto ingresado por el usuario y muestra información relevante sobre él.

## ⚙️ Explicación
- Se pidió al usuario un texto completo con `input()`.  
- Se normalizó el texto con `.lower()` para evitar problemas de mayúsculas/minúsculas.  
- Se solicitaron tres letras y se contó cuántas veces aparecían con `.count()`.  
- Se calculó el número de palabras usando `.split()` y `len()`.  
- Se mostró la primera y última letra del texto con indexación `[0]` y `[-1]`.  
- Se invirtió el orden de las palabras con `.reverse()` y `" ".join()`.  
- Se verificó si la palabra **"Python"** estaba presente usando el operador `in`.  

---

# ✅ Solución
El reto pedía analizar un texto y mostrar estadísticas básicas.  
La solución fue usar **variables